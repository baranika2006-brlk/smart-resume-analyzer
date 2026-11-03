from flask import Blueprint, request, jsonify, session
from bson.objectid import ObjectId
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from database.database import (
    get_users_col, get_job_roles_col, 
    get_resumes_col, get_analysis_results_col, 
    get_reviews_col
)

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

# Helper security guard
def is_admin():
    # Allow if session says role is admin or header parameter passed
    if session.get("user_role") == "admin":
        return True
    admin_secret = request.headers.get("X-Admin-Access")
    return admin_secret == "AdminSecret2026"

@admin_bp.route("/stats", methods=["GET"])
def get_admin_stats():
    try:
        users_col = get_users_col()
        job_roles_col = get_job_roles_col()
        resumes_col = get_resumes_col()
        analysis_col = get_analysis_results_col()
        reviews_col = get_reviews_col()

        total_users = users_col.count_documents({})
        total_job_roles = job_roles_col.count_documents({})
        total_resumes = resumes_col.count_documents({})
        total_analyses = analysis_col.count_documents({})
        total_reviews = reviews_col.count_documents({})

        # Calculate average overall platform score
        all_analyses = list(analysis_col.find({}, {"overall_score": 1}))
        if all_analyses:
            avg_platform_score = round(sum(a.get("overall_score", 0) for a in all_analyses) / len(all_analyses), 1)
        else:
            avg_platform_score = 0.0

        return jsonify({
            "success": True,
            "stats": {
                "total_users": total_users,
                "total_job_roles": total_job_roles,
                "total_resumes": total_resumes,
                "total_analyses": total_analyses,
                "total_reviews": total_reviews,
                "avg_platform_score": avg_platform_score
            }
        }), 200
    except Exception as e:
        print(f"[ERROR] Admin stats error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@admin_bp.route("/users", methods=["GET"])
def get_all_users():
    try:
        users_col = get_users_col()
        users = []
        for u in users_col.find({}):
            users.append({
                "id": str(u["_id"]),
                "name": u.get("name"),
                "email": u.get("email"),
                "role": u.get("role", "user"),
                "created_at": u.get("created_at")
            })
        return jsonify({"success": True, "users": users}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@admin_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        users_col = get_users_col()
        res = users_col.delete_one({"_id": ObjectId(user_id)}) if ObjectId.is_valid(user_id) else None
        if res and res.deleted_count > 0:
            return jsonify({"success": True, "message": "User deleted successfully."}), 200
        return jsonify({"success": False, "message": "User not found."}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@admin_bp.route("/job-roles", methods=["POST"])
def add_job_role():
    try:
        data = request.get_json() or {}
        title = data.get("title", "").strip()
        role_id = data.get("role_id") or title.lower().replace(" ", "-")
        category = data.get("category", "General Tech").strip()
        description = data.get("description", "").strip()
        required_skills = [s.strip() for s in data.get("required_skills", []) if s.strip()]
        soft_skills = [s.strip() for s in data.get("soft_skills", []) if s.strip()]
        certifications = [s.strip() for s in data.get("recommended_certifications", []) if s.strip()]
        projects = [s.strip() for s in data.get("suggested_projects", []) if s.strip()]

        if not title or not required_skills:
            return jsonify({"success": False, "message": "Title and required skills are mandatory."}), 400

        col = get_job_roles_col()
        existing = col.find_one({"role_id": role_id})
        
        doc = {
            "role_id": role_id,
            "title": title,
            "category": category,
            "description": description,
            "required_skills": required_skills,
            "soft_skills": soft_skills,
            "recommended_certifications": certifications,
            "suggested_projects": projects,
            "experience_level": data.get("experience_level", "Entry Level"),
            "created_at": datetime.utcnow().isoformat()
        }

        if existing:
            col.update_one({"role_id": role_id}, {"$set": doc})
            msg = "Job role updated successfully!"
        else:
            col.insert_one(doc)
            msg = "Job role created successfully!"

        return jsonify({"success": True, "message": msg}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@admin_bp.route("/job-roles/<identifier>", methods=["DELETE"])
def delete_job_role(identifier):
    try:
        col = get_job_roles_col()
        filter_q = {"role_id": identifier}
        if ObjectId.is_valid(identifier):
            filter_q = {"$or": [{"role_id": identifier}, {"_id": ObjectId(identifier)}]}

        res = col.delete_one(filter_q)
        if res.deleted_count > 0:
            return jsonify({"success": True, "message": "Job role deleted successfully."}), 200
        return jsonify({"success": False, "message": "Job role not found."}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@admin_bp.route("/resumes", methods=["GET"])
def get_all_resumes():
    try:
        col = get_resumes_col()
        resumes = []
        for r in col.find({}).sort("upload_date", -1).limit(50):
            resumes.append({
                "id": str(r["_id"]),
                "user_id": r.get("user_id"),
                "filename": r.get("filename"),
                "file_size_kb": round(r.get("file_size", 0) / 1024, 1),
                "upload_date": r.get("upload_date")
            })
        return jsonify({"success": True, "resumes": resumes}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@admin_bp.route("/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    try:
        col = get_reviews_col()
        res = col.delete_one({"_id": ObjectId(review_id)}) if ObjectId.is_valid(review_id) else None
        if res and res.deleted_count > 0:
            return jsonify({"success": True, "message": "Review deleted successfully."}), 200
        return jsonify({"success": False, "message": "Review not found."}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
