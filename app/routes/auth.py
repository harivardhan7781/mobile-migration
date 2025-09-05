from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "guest")
    # demo-only token
    return jsonify({"token": f"demo-token-{username}", "user": username}), 200
