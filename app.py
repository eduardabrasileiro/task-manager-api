from flask import Flask, jsonify
from routes.tasks import bp as tasks_bp
from db import init_db

def create_app():
    app = Flask(__name__)
    app.config["DATABASE_PATH"] = "tasks.db"
    init_db(app)
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    @app.get("/")
    def index():
        return jsonify({"status": "ok", "service": "Task Manager API"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)