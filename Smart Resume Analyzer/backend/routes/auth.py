from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from bson.objectid import ObjectId
import re
import sys
import os

# Import DB accessor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from database.database import get_users_col

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def sanitize_user(user_doc):
    """Remove sensitive password_hash from user dictionary."""
    if not user_doc:
        return None
    return {
        "id": str(user_doc["_id"]),
        "name": user_doc.get("name"),
        "email": user_doc.get("email"),
        "role": user_doc.get("role", "user"),
        "created_at": user_doc.get("created_at")
    }

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json() or {}
        name = data.get("name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        if not name or not email or not password:
            return jsonify({"success": False, "message": "Name, email, and password are required."}), 400

        if not re.match(EMAIL_REGEX, email):
            return jsonify({"success": False, "message": "Please enter a valid email address."}), 400

        if len(password) < 6:
            return jsonify({"success": False, "message": "Password must be at least 6 characters long."}), 400

        users_col = get_users_col()
        if users_col.find_one({"email": email}):
            return jsonify({"success": False, "message": "An account with this email already exists."}), 409

        password_hash = generate_password_hash(password)
        new_user = {
            "name": name,
            "email": email,
            "password_hash": password_hash,
            "role": "user",
            "created_at": datetime.utcnow().isoformat()
        }

        result = users_col.insert_one(new_user)
        new_user["_id"] = result.inserted_id

        user_data = sanitize_user(new_user)
        session["user_id"] = user_data["id"]
        session["user_name"] = user_data["name"]
        session["user_email"] = user_data["email"]
        session["user_role"] = user_data["role"]

        return jsonify({
            "success": True,
            "message": "Registration successful! Welcome to Smart Resume Analyzer.",
            "user": user_data
        }), 201

    except Exception as e:
        print(f"[ERROR] Registration error: {e}")
        return jsonify({"success": False, "message": f"Server error during registration: {str(e)}"}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json() or {}
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        if not email or not password:
            return jsonify({"success": False, "message": "Email and password are required."}), 400

        users_col = get_users_col()
        user = users_col.find_one({"email": email})

        if not user or not check_password_hash(user["password_hash"], password):
            return jsonify({"success": False, "message": "Invalid email or password."}), 401

        user_data = sanitize_user(user)
        session["user_id"] = user_data["id"]
        session["user_name"] = user_data["name"]
        session["user_email"] = user_data["email"]
        session["user_role"] = user_data["role"]

        return jsonify({
            "success": True,
            "message": f"Welcome back, {user_data['name']}!",
            "user": user_data
        }), 200

    except Exception as e:
        print(f"[ERROR] Login error: {e}")
        return jsonify({"success": False, "message": f"Server error during login: {str(e)}"}), 500

@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True, "message": "Logged out successfully."}), 200

@auth_bp.route("/me", methods=["GET"])
def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "message": "Not authenticated", "user": None}), 200

    try:
        users_col = get_users_col()
        user = users_col.find_one({"_id": ObjectId(user_id)})
        if not user:
            session.clear()
            return jsonify({"success": False, "message": "User not found", "user": None}), 200

        return jsonify({"success": True, "user": sanitize_user(user)}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e), "user": None}), 500
