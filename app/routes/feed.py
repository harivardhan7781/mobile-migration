from flask import Blueprint, jsonify, request
from datetime import datetime

feed_bp = Blueprint("feed", __name__)
_FEED = [{"id": 1, "text": "Welcome!", "ts": datetime.utcnow().isoformat()}]

@feed_bp.get("/")
def list_items():
    return jsonify({"items": _FEED, "count": len(_FEED)}), 200

@feed_bp.post("/")
def add_item():
    data = request.get_json(silent=True) or {}
    item = {
        "id": len(_FEED) + 1,
        "text": data.get("text", ""),
        "ts": datetime.utcnow().isoformat(),
    }
    _FEED.append(item)
    return jsonify(item), 201
