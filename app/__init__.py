import os
from flask import Flask


def create_app(deployment="production"):
    flask_app = Flask(__name__, static_folder='./dist')
    config_app(flask_app)
    with flask_app.app_context():
        from app import database
        from app import routes
        from app import models
        from app.api import api_bp
        flask_app.register_blueprint(api_bp, url_prefix='/api')

    return flask_app


def config_app(app) -> None:
    pg_database = app.config['POSTGRES_DB'] = os.environ.get('POSTGRES_DB', "gis")
    pg_host = app.config['POSTGRES_HOST'] = os.environ.get('POSTGRES_HOST', "localhost")
    pg_port = app.config['POSTGRES_PORT'] = os.environ.get('POSTGRES_PORT', 5432)
    pg_user = app.config['POSTGRES_USER'] = os.environ.get('POSTGRES_USER', "gis")
    pg_pwd = app.config['POSTGRES_PASSWORD'] = os.environ.get('POSTGRES_PASSWORD', "postgres")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{pg_user}:{pg_pwd}@{pg_host}:{pg_port}/{pg_database}"
    app.config['GEOSERVER_URL'] = os.environ.get('GEOSERVER_URL', "http://127.0.0.1:8080")
    app.config['GEOSERVER_ADMIN_USER'] = os.environ.get('GEOSERVER_ADMIN_USER', "admin")
    app.config['GEOSERVER_ADMIN_PASSWORD'] = os.environ.get('GEOSERVER_ADMIN_PASSWORD', "geoserver")
    app.config['GEOSERVER_WORKSPACE'] = os.environ.get('GEOSERVER_WORKSPACE', "default")
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False