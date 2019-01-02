
from sqlalchemy.dialects.postgresql import JSON

from database import db

# ToDo - add Mentee, Mentor, Meeting classes

class Mentee(db.Model):
    __tablename__ = 'mentees'

    id = db.Column(db.Integer, primary_key=True)
    # ToDo - add column definitions

    # ToDo - add relationship (1 mentor has many mentees)
    # ToDo - add relationship (1 mentor is active for one cycle)


class Mentor(db.Model):
    __tablename__ = 'mentors'

    id = db.Column(db.Integer, primary_key=True)
    # ToDo - add column definitions

    # ToDo - add relationship (1 mentor has many mentees)

class Meetings(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    # ToDo - add column definitions

    # ToDo - add relationship (A meeting takes place sometime between 1 mentor and 1 mentee)

class Cycles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(50))
    cycle_start = db.Column(db.DateTime)
    cycle_end = db.Column(db.DateTime)

# Fixme - delete example class below
class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __repr__(self):
        return '<id {}>'.format(self.id)
