from flask import Blueprint, jsonify
from bson.objectid import ObjectId
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from database.database import get_job_roles_col

job_roles_bp = Blueprint("job_roles", __name__, url_prefix="/api/job-roles")

def serialize_role(role_doc):
    if not role_doc:
        return None
    return {
        "id": str(role_doc["_id"]),
        "role_id": role_doc.get("role_id", str(role_doc["_id"])),
        "title": role_doc.get("title"),
        "category": role_doc.get("category"),
        "description": role_doc.get("description"),
        "required_skills": role_doc.get("required_skills", []),
        "soft_skills": role_doc.get("soft_skills", []),
        "recommended_certifications": role_doc.get("recommended_certifications", []),
        "suggested_projects": role_doc.get("suggested_projects", []),
        "experience_level": role_doc.get("experience_level", "Entry Level")
    }

@job_roles_bp.route("", methods=["GET"])
def get_all_job_roles():
    try:
        job_roles_col = get_job_roles_col()
        roles_cursor = job_roles_col.find({})
        roles_list = [serialize_role(doc) for doc in roles_cursor]
        return jsonify({"success": True, "job_roles": roles_list}), 200
    except Exception as e:
        print(f"[ERROR] Fetching job roles failed: {e}")
        return jsonify({"success": False, "message": f"Failed to load job roles: {str(e)}"}), 500

@job_roles_bp.route("/<identifier>", methods=["GET"])
def get_job_role(identifier):
    try:
        job_roles_col = get_job_roles_col()
        role = None
        
        # Try finding by role_id first, then by ObjectId
        role = job_roles_col.find_one({"role_id": identifier})
        if not role and ObjectId.is_valid(identifier):
            role = job_roles_col.find_one({"_id": ObjectId(identifier)})

        if not role:
            return jsonify({"success": False, "message": "Job role not found."}), 404

        return jsonify({"success": True, "job_role": serialize_role(role)}), 200
    except Exception as e:
        print(f"[ERROR] Fetching single job role failed: {e}")
        return jsonify({"success": False, "message": str(e)}), 500
