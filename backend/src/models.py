from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, check_password_hash

from database import db


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
    __tablename__ = "cycles"

    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(50))
    cycle_start = db.Column(db.DateTime)
    cycle_end = db.Column(db.DateTime)

class Users(UserMixin, db.Model):
    __tablename__ = "pre_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, id):
        self.id = id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)