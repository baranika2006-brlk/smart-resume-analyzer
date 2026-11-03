import os
from pymongo import MongoClient, errors

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017/")
DB_NAME = os.getenv("DB_NAME", "smart_resume_analyzer")

_client = None

def get_mongo_client():
    global _client
    if _client is None:
        try:
            _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
            # Test connection
            _client.admin.command('ping')
        except errors.ConnectionFailure as e:
            print(f"[ERROR] Failed to connect to MongoDB at {MONGO_URI}: {e}")
            raise e
    return _client

def get_db():
    client = get_mongo_client()
    return client[DB_NAME]

def get_collection(collection_name):
    db = get_db()
    return db[collection_name]

# Helper collection accessors
def get_users_col():
    return get_collection("users")

def get_job_roles_col():
    return get_collection("job_roles")

def get_resumes_col():
    return get_collection("resumes")

def get_analysis_results_col():
    return get_collection("analysis_results")

def get_suggestions_col():
    return get_collection("suggestions")

def get_reviews_col():
    return get_collection("reviews")
