from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register routes
    from app.controllers.user_controller import user_bp

    app.register_blueprint(user_bp)

    return app
