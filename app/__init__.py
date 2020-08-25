from flask import Flask, Blueprint
from flask import Blueprint, render_template


def create_app():
    flask_app = Flask( __name__, static_folder='./dist')
    with flask_app.app_context():
        from app import routes

    return flask_app
