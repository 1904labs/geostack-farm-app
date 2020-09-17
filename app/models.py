from .database import db
from sqlalchemy.dialects.postgresql import JSON


class Points(db.Model):
    __tablename__ = 'points'

    id = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.String())

    def __init__(self, point):
        self.point = point

    def __repr__(self):
        return '<id {}>'.format(self.id)