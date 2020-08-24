from flask import Flask
from config import Config

def create_app(config_class=Config):
    flask_app = Flask(
        __name__,
        static_folder = './dist/static',
        template_folder="./dist"
    )
    flask_app.config.from_object(config_class)
    
    with flask_app.app_context():
        from app import routes

    return flask_app