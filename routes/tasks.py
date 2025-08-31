from flask import Blueprint, request, jsonify
import models

bp = Blueprint("tasks", __name__)

@bp.get("/")
def list_tasks():
    return jsonify(models.fetch_all())

@bp.post("/")
def create_task():
    if not request.is_json:
        return jsonify({"error": "expected JSON"}), 415
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400
    task = models.create(title)
    return jsonify(task), 201

@bp.get("/<int:task_id>")
def get_task(task_id: int):
    task = models.fetch_one(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(task)

@bp.put("/<int:task_id>/done")
def mark_done(task_id: int):
    if not models.fetch_one(task_id):
        return jsonify({"error": "not found"}), 404
    return jsonify(models.set_done(task_id, True))

@bp.put("/<int:task_id>/undone")
def mark_undone(task_id: int):
    if not models.fetch_one(task_id):
        return jsonify({"error": "not found"}), 404
    return jsonify(models.set_done(task_id, False))

@bp.delete("/<int:task_id>")
def remove_task(task_id: int):
    ok = models.delete(task_id)
    if not ok:
        return jsonify({"error": "not found"}), 404
    return "", 204