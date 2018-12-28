
from sqlalchemy.dialects.postgresql import JSON

from src.database import db

# ToDo - add Mentee, Mentor, Meeting classes

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __repr__(self):
        return '<id {}>'.format(self.id)
