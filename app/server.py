from flask import Flask
from app.routes.health import health_bp
from app.routes.feed import feed_bp
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(feed_bp, url_prefix="/feed")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
