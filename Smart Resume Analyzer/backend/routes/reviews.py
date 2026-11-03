from flask import Blueprint, request, jsonify, session
from datetime import datetime
from bson.objectid import ObjectId
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from database.database import get_reviews_col

reviews_bp = Blueprint("reviews", __name__, url_prefix="/api/reviews")

def serialize_review(doc):
    if not doc:
        return None
    return {
        "id": str(doc["_id"]),
        "user_name": doc.get("user_name", "Anonymous"),
        "rating": doc.get("rating", 5),
        "comment": doc.get("comment", ""),
        "created_at": doc.get("created_at")
    }

@reviews_bp.route("", methods=["GET"])
def get_reviews():
    try:
        col = get_reviews_col()
        reviews_cursor = col.find({}).sort("created_at", -1).limit(50)
        reviews_list = [serialize_review(doc) for doc in reviews_cursor]
        
        # Calculate summary average rating
        if reviews_list:
            avg_rating = round(sum(r["rating"] for r in reviews_list) / len(reviews_list), 1)
        else:
            avg_rating = 5.0

        return jsonify({
            "success": True,
            "reviews": reviews_list,
            "total_reviews": len(reviews_list),
            "average_rating": avg_rating
        }), 200
    except Exception as e:
        print(f"[ERROR] Fetch reviews error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@reviews_bp.route("", methods=["POST"])
def add_review():
    try:
        data = request.get_json() or {}
        rating = int(data.get("rating", 5))
        comment = data.get("comment", "").strip()
        user_name = data.get("user_name") or session.get("user_name") or "Anonymous Job Seeker"
        user_id = session.get("user_id") or "guest"

        if rating < 1 or rating > 5:
            return jsonify({"success": False, "message": "Rating must be between 1 and 5 stars."}), 400

        if not comment:
            return jsonify({"success": False, "message": "Please enter a comment for your review."}), 400

        col = get_reviews_col()
        review_doc = {
            "user_id": str(user_id),
            "user_name": user_name,
            "rating": rating,
            "comment": comment,
            "created_at": datetime.utcnow().isoformat()
        }
        res = col.insert_one(review_doc)
        review_doc["_id"] = res.inserted_id

        return jsonify({
            "success": True,
            "message": "Thank you for your rating and feedback!",
            "review": serialize_review(review_doc)
        }), 201
    except Exception as e:
        print(f"[ERROR] Add review error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500
