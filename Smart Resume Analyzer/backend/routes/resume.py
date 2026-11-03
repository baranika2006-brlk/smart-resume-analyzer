import os
import sys
import re
from datetime import datetime
from flask import Blueprint, request, jsonify, session, current_app
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from database.database import (
    get_job_roles_col, get_resumes_col, 
    get_analysis_results_col, get_suggestions_col
)
try:
    from backend.services.text_extractor import extract_resume_text
    from backend.services.skill_extractor import extract_skills_nlp
    from backend.services.analyzer import analyze_resume_against_role
    from backend.services.scorer import calculate_resume_score
    from backend.services.suggestions import generate_personalized_suggestions
except ImportError:
    from services.text_extractor import extract_resume_text
    from services.skill_extractor import extract_skills_nlp
    from services.analyzer import analyze_resume_against_role
    from services.scorer import calculate_resume_score
    from services.suggestions import generate_personalized_suggestions

resume_bp = Blueprint("resume", __name__, url_prefix="/api/resume")

def allowed_file(filename):
    if not filename or '.' not in filename:
        return True
    return filename.rsplit('.', 1)[1].lower() in {'pdf', 'docx', 'txt'}

@resume_bp.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        # 1. Validation & Input Extraction
        if 'resume_file' not in request.files:
            return jsonify({"success": False, "message": "No resume file was received. Please select a PDF or DOCX file."}), 400

        file = request.files['resume_file']
        role_id = (request.form.get("role_id") or "").strip()
        user_id = request.form.get("user_id") or session.get("user_id") or "anonymous_guest"

        if file.filename == '':
            return jsonify({"success": False, "message": "No file selected."}), 400

        # 2. Fetch Target Job Role from MongoDB with multiple fallbacks
        job_roles_col = get_job_roles_col()
        target_role = None

        if role_id:
            target_role = job_roles_col.find_one({"role_id": role_id})
            if not target_role:
                target_role = job_roles_col.find_one({"title": {"$regex": f"^{re.escape(role_id)}$", "$options": "i"}})
            if not target_role and ObjectId.is_valid(role_id):
                target_role = job_roles_col.find_one({"_id": ObjectId(role_id)})

        # If role not found, fallback to first available role in DB
        if not target_role:
            target_role = job_roles_col.find_one({})

        if not target_role:
            return jsonify({"success": False, "message": "No job roles available in database. Please run initialization."}), 500

        # 3. Securely Save File
        filename = secure_filename(file.filename) or "uploaded_resume.pdf"
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_")
        saved_filename = f"{timestamp}{filename}"
        
        upload_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../uploads"))
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, saved_filename)
        
        file.save(filepath)
        file_size = os.path.getsize(filepath)

        # 4. Store Resume Metadata in MongoDB
        try:
            resumes_col = get_resumes_col()
            resume_doc = {
                "user_id": str(user_id),
                "filename": filename,
                "saved_filename": saved_filename,
                "filepath": filepath,
                "file_size": file_size,
                "upload_date": datetime.utcnow().isoformat()
            }
            res_insert = resumes_col.insert_one(resume_doc)
            resume_id = str(res_insert.inserted_id)
        except Exception as db_err:
            print(f"[WARN] Resume metadata store error: {db_err}")
            resume_id = "temp_resume"

        # 5. Text Extraction
        extracted_text = extract_resume_text(filepath)
        if not extracted_text:
            extracted_text = f"Resume document {filename}"

        # 6. Skill Extraction using NLP
        extracted_skills = extract_skills_nlp(extracted_text)

        # 7. Skill Comparison & Gap Analysis
        analysis_data = analyze_resume_against_role(extracted_skills, target_role)

        # 8. Overall Score Calculation out of 100
        score_data = calculate_resume_score(analysis_data, extracted_skills)

        # 9. Recommendation & Suggestion Generation
        suggestions_data = generate_personalized_suggestions(analysis_data, target_role, score_data)

        # 10. Store Analysis Result in MongoDB
        analysis_id = "temp_analysis"
        try:
            analysis_col = get_analysis_results_col()
            analysis_record = {
                "user_id": str(user_id),
                "resume_id": resume_id,
                "job_role_id": target_role.get("role_id", str(target_role.get("_id"))),
                "job_role_title": target_role.get("title", "Selected Role"),
                "overall_score": score_data["overall_score"],
                "grade": score_data["grade"],
                "score_breakdown": score_data["breakdown"],
                "skill_match_percentage": analysis_data["skill_match_percentage"],
                "matched_skills": analysis_data["matched_skills"],
                "missing_skills": analysis_data["missing_skills"],
                "matched_soft_skills": analysis_data["matched_soft_skills"],
                "missing_soft_skills": analysis_data["missing_soft_skills"],
                "extracted_skills": extracted_skills,
                "created_at": datetime.utcnow().isoformat()
            }
            analysis_insert = analysis_col.insert_one(analysis_record)
            analysis_id = str(analysis_insert.inserted_id)

            # Store Suggestions
            suggestions_col = get_suggestions_col()
            suggestions_record = {
                "analysis_id": analysis_id,
                "user_id": str(user_id),
                "missing_skills_suggestions": suggestions_data.get("missing_skills_suggestions", []),
                "recommended_certifications": suggestions_data.get("recommended_certifications", []),
                "recommended_projects": suggestions_data.get("recommended_projects", []),
                "recommended_keywords": suggestions_data.get("recommended_keywords", []),
                "general_tips": suggestions_data.get("general_tips", []),
                "created_at": datetime.utcnow().isoformat()
            }
            suggestions_col.insert_one(suggestions_record)
        except Exception as db_save_err:
            print(f"[WARN] DB Analysis save notice: {db_save_err}")

        # 11. Return Complete JSON Response
        return jsonify({
            "success": True,
            "message": "Resume successfully analyzed!",
            "analysis_id": analysis_id,
            "job_role": {
                "role_id": target_role.get("role_id"),
                "title": target_role.get("title"),
                "category": target_role.get("category")
            },
            "overall_score": score_data["overall_score"],
            "grade": score_data["grade"],
            "score_breakdown": score_data["breakdown"],
            "skill_match_percentage": analysis_data["skill_match_percentage"],
            "matched_skills": analysis_data["matched_skills"],
            "missing_skills": analysis_data["missing_skills"],
            "matched_soft_skills": analysis_data["matched_soft_skills"],
            "missing_soft_skills": analysis_data["missing_soft_skills"],
            "extracted_skills": extracted_skills,
            "suggestions": suggestions_data
        }), 200

    except Exception as e:
        print(f"[ERROR] Resume analysis failed: {e}")
        return jsonify({"success": False, "message": f"Resume analysis failed: {str(e)}"}), 500
