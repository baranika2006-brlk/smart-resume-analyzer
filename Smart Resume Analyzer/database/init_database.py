import sys
import os
from datetime import datetime

# Setup path so parent folder is accessible
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from database.database import (
        get_db, get_users_col, get_job_roles_col, 
        get_reviews_col, get_resumes_col, 
        get_analysis_results_col, get_suggestions_col
    )
    from database.sample_data import SAMPLE_JOB_ROLES, DEFAULT_ADMIN_USER, SAMPLE_REVIEWS
except ModuleNotFoundError:
    from database import (
        get_db, get_users_col, get_job_roles_col, 
        get_reviews_col, get_resumes_col, 
        get_analysis_results_col, get_suggestions_col
    )
    from sample_data import SAMPLE_JOB_ROLES, DEFAULT_ADMIN_USER, SAMPLE_REVIEWS

from werkzeug.security import generate_password_hash

def initialize_database():
    print("==================================================")
    print(" Starting MongoDB Database Initialization...")
    print("==================================================")
    
    try:
        db = get_db()
        print(f"[SUCCESS] Connected to MongoDB database: '{db.name}'")
    except Exception as e:
        print(f"[FATAL ERROR] Could not connect to MongoDB server: {e}")
        print("Please ensure MongoDB Server is installed and running on mongodb://127.0.0.1:27017/")
        sys.exit(1)

    # 1. Ensure Collections Exist & Set Unique Indexes
    users_col = get_users_col()
    job_roles_col = get_job_roles_col()
    reviews_col = get_reviews_col()
    get_resumes_col()
    get_analysis_results_col()
    get_suggestions_col()

    try:
        users_col.create_index("email", unique=True)
        print("[SUCCESS] Created unique index on 'users.email'")
    except Exception as e:
        print(f"[INFO] Index on users.email already exists or info: {e}")

    # 2. Insert Sample Job Roles
    inserted_roles = 0
    updated_roles = 0
    for role in SAMPLE_JOB_ROLES:
        filter_query = {"role_id": role["role_id"]}
        existing = job_roles_col.find_one(filter_query)
        if existing:
            job_roles_col.update_one(filter_query, {"$set": role})
            updated_roles += 1
        else:
            role["created_at"] = datetime.utcnow().isoformat()
            job_roles_col.insert_one(role)
            inserted_roles += 1

    print(f"[SUCCESS] Job Roles synced: {inserted_roles} inserted, {updated_roles} updated.")

    # 3. Create Default Admin User
    admin_email = DEFAULT_ADMIN_USER["email"]
    existing_admin = users_col.find_one({"email": admin_email})
    if not existing_admin:
        admin_doc = {
            "name": DEFAULT_ADMIN_USER["name"],
            "email": admin_email,
            "password_hash": generate_password_hash("Admin@123"),
            "role": "admin",
            "created_at": datetime.utcnow().isoformat()
        }
        users_col.insert_one(admin_doc)
        print(f"[SUCCESS] Created default admin account: {admin_email} (Password: Admin@123)")
    else:
        print(f"[INFO] Default admin account '{admin_email}' already present.")

    # 4. Insert Initial Sample Reviews if empty
    if reviews_col.count_documents({}) == 0:
        for rev in SAMPLE_REVIEWS:
            rev["created_at"] = datetime.utcnow().isoformat()
            reviews_col.insert_one(rev)
        print(f"[SUCCESS] Inserted {len(SAMPLE_REVIEWS)} sample user reviews.")
    else:
        print("[INFO] User reviews collection already initialized.")

    print("==================================================")
    print(" Database Initialization Completed Successfully!")
    print("==================================================")
    return True

if __name__ == "__main__":
    initialize_database()
