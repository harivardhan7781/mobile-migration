from flask import Blueprint, jsonify
from datetime import datetime

# Define a Blueprint for health routes
health_bp = Blueprint("health", __name__)

@health_bp.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "time": datetime.utcnow().isoformat()
    }), 200
