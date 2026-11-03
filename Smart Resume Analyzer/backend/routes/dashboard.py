from flask import Blueprint, jsonify, session, request
from bson.objectid import ObjectId
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from database.database import get_analysis_results_col, get_suggestions_col

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/api/dashboard")

def serialize_analysis(doc):
    if not doc:
        return None
    return {
        "id": str(doc["_id"]),
        "resume_id": doc.get("resume_id"),
        "job_role_id": doc.get("job_role_id"),
        "job_role_title": doc.get("job_role_title", "Custom Role"),
        "overall_score": doc.get("overall_score", 0),
        "grade": doc.get("grade", "N/A"),
        "skill_match_percentage": doc.get("skill_match_percentage", 0),
        "matched_skills": doc.get("matched_skills", []),
        "missing_skills": doc.get("missing_skills", []),
        "extracted_skills": doc.get("extracted_skills", {}),
        "score_breakdown": doc.get("score_breakdown", {}),
        "created_at": doc.get("created_at")
    }

@dashboard_bp.route("/stats", methods=["GET"])
def get_user_stats():
    user_id = request.args.get("user_id") or session.get("user_id") or "anonymous_guest"
    try:
        col = get_analysis_results_col()
        records = list(col.find({"user_id": str(user_id)}))
        
        total_analyses = len(records)
        if total_analyses == 0:
            return jsonify({
                "success": True,
                "stats": {
                    "total_analyses": 0,
                    "highest_score": 0,
                    "avg_score": 0,
                    "latest_role": "None"
                }
            }), 200

        scores = [r.get("overall_score", 0) for r in records]
        highest_score = max(scores)
        avg_score = round(sum(scores) / total_analyses, 1)

        # Get latest
        records_sorted = sorted(records, key=lambda x: x.get("created_at", ""), reverse=True)
        latest_role = records_sorted[0].get("job_role_title", "N/A")

        return jsonify({
            "success": True,
            "stats": {
                "total_analyses": total_analyses,
                "highest_score": highest_score,
                "avg_score": avg_score,
                "latest_role": latest_role
            }
        }), 200
    except Exception as e:
        print(f"[ERROR] Dashboard stats error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@dashboard_bp.route("/history", methods=["GET"])
def get_user_history():
    user_id = request.args.get("user_id") or session.get("user_id") or "anonymous_guest"
    try:
        col = get_analysis_results_col()
        cursor = col.find({"user_id": str(user_id)}).sort("created_at", -1).limit(20)
        history = [serialize_analysis(doc) for doc in cursor]
        return jsonify({"success": True, "history": history}), 200
    except Exception as e:
        print(f"[ERROR] Fetch history error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@dashboard_bp.route("/analysis/<analysis_id>", methods=["GET"])
def get_analysis_detail(analysis_id):
    try:
        col = get_analysis_results_col()
        doc = col.find_one({"_id": ObjectId(analysis_id)}) if ObjectId.is_valid(analysis_id) else None
        if not doc:
            return jsonify({"success": False, "message": "Analysis record not found."}), 404

        analysis_serialized = serialize_analysis(doc)
        
        # Fetch suggestions
        sug_col = get_suggestions_col()
        sug_doc = sug_col.find_one({"analysis_id": str(doc["_id"])})
        suggestions = {}
        if sug_doc:
            suggestions = {
                "missing_skills_suggestions": sug_doc.get("missing_skills_suggestions", []),
                "recommended_certifications": sug_doc.get("recommended_certifications", []),
                "recommended_projects": sug_doc.get("recommended_projects", []),
                "recommended_keywords": sug_doc.get("recommended_keywords", []),
                "general_tips": sug_doc.get("general_tips", [])
            }

        return jsonify({
            "success": True,
            "analysis": analysis_serialized,
            "suggestions": suggestions
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
