import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "smart_resume_analyzer_secret_key_2026")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017/")
    DB_NAME = os.getenv("DB_NAME", "smart_resume_analyzer")

    # Session / Cookie settings (cross-origin frontend on :5500 <-> API on :5000)
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = False   # Set True only in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True

    # Upload Configurations
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB max file size
    ALLOWED_EXTENSIONS = {"pdf", "docx"}

    @staticmethod
    def init_app(app):
        # Create uploads folder if it doesn't exist
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
