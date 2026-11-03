import os
import sys
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

# Adjust module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from backend.config import Config
    from backend.routes.auth import auth_bp
    from backend.routes.job_roles import job_roles_bp
    from backend.routes.resume import resume_bp
    from backend.routes.dashboard import dashboard_bp
    from backend.routes.reviews import reviews_bp
    from backend.routes.admin import admin_bp
except ImportError:
    from config import Config
    from routes.auth import auth_bp
    from routes.job_roles import job_roles_bp
    from routes.resume import resume_bp
    from routes.dashboard import dashboard_bp
    from routes.reviews import reviews_bp
    from routes.admin import admin_bp
from database.database import get_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    # Enable CORS for all local development origins and null (file:// protocol)
    CORS(app,
         supports_credentials=True,
         resources={r"/api/*": {"origins": "*"}},
         allow_headers=["Content-Type", "Authorization", "X-Admin-Access", "Accept", "Origin", "X-Requested-With"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    )

    # Global CORS Header Injector for full cross-origin compatibility
    @app.after_request
    def add_cors_headers(response):
        origin = request.headers.get("Origin")
        if origin:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Admin-Access, Accept, Origin, X-Requested-With"
        else:
            response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = app.make_default_options_response()
            origin = request.headers.get("Origin")
            if origin:
                response.headers["Access-Control-Allow-Origin"] = origin
                response.headers["Access-Control-Allow-Credentials"] = "true"
                response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
                response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Admin-Access, Accept, Origin, X-Requested-With"
            return response

    # Register API Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(job_roles_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(admin_bp)

    # Serve Frontend Static Files Directly on Port 5000
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))

    @app.route("/", methods=["GET"])
    def serve_index():
        return send_from_directory(frontend_dir, "index.html")

    @app.route("/<path:filename>", methods=["GET"])
    def serve_frontend(filename):
        # Don't intercept API routes
        if filename.startswith("api/"):
            return jsonify({"success": False, "message": "API endpoint not found."}), 404
        
        filepath = os.path.join(frontend_dir, filename)
        if os.path.isfile(filepath):
            return send_from_directory(frontend_dir, filename)
        if os.path.isfile(filepath + ".html"):
            return send_from_directory(frontend_dir, filename + ".html")
        return send_from_directory(frontend_dir, "index.html")

    # Global API Error Handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "message": f"Bad Request: {str(error)}"}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": "API endpoint or resource not found."}), 404

    @app.errorhandler(413)
    def file_too_large(error):
        return jsonify({"success": False, "message": "File exceeds maximum size limit of 5 MB."}), 413

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"success": False, "message": f"Internal Server Error: {str(error)}"}), 500

    @app.route("/api/health", methods=["GET"])
    def health_check():
        try:
            db = get_db()
            db.command('ping')
            db_status = "Connected"
        except Exception as e:
            db_status = f"Disconnected ({str(e)})"

        return jsonify({
            "status": "online",
            "application": "Smart Resume Analyzer API",
            "version": "1.0.0",
            "mongodb_status": db_status
        }), 200

    return app

if __name__ == "__main__":
    import flask.cli
    import logging
    # Suppress development server banner & warning messages
    flask.cli.show_server_banner = lambda *args: None
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    app = create_app()
    port = int(os.getenv("PORT", 5000))
    print("==================================================")
    print(f" Smart Resume Analyzer Backend Active on Port {port}")
    print(f" Web UI:  http://127.0.0.1:{port}/")
    print(f" API URL: http://127.0.0.1:{port}/api")
    print("==================================================")
    app.run(host="0.0.0.0", port=port, debug=False)

