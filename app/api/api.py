from flask import Blueprint
from flask_restx import Api

__all__ = ['rp', 'bp']

bp = Blueprint('api', __name__)
rp = Api(bp)
