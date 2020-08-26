from flask import Flask


def create_app(deployment="production"):
    flask_app = Flask(__name__, static_folder='./dist')
    with flask_app.app_context():
        from app import routes
        from app.api import api_bp
        flask_app.register_blueprint(api_bp, url_prefix='/api')

    return flask_app
