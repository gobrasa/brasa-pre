import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from database import db


class ExamSchedule(db.Model):
    __tablename__ = 'scheduled_exams'

    # 1 mentee, many exam schedules
    id = db.Column(db.Integer, primary_key=True)
    realization_date = db.Column(db.DateTime, nullable=False)
    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)

    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'))
    exam = db.relationship("Exams")
    score = db.Column(db.String(20))  # Not sure whether score is A or 100


class Mentee(db.Model):
    __tablename__ = 'mentees'

    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'))
    username = db.Column(db.String(64), db.ForeignKey('pre_users.username'), unique=True, index=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    financial_aid = db.Column(db.Boolean, nullable=False)
    cycle_id = db.Column(db.Integer, db.ForeignKey('cycles.id'))

    # Exam schedule
    exam_schedules = db.relationship("ExamSchedule")

    # ToDo - add relationship to universities
    # ToDo - add relationship (1 mentee has 1 cycle)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'mentor_id': self.mentor_id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name' : self.last_name,
            'city' : self.city,
            'state': self.state,
            'financial_aid': self.financial_aid,
            'cycle_id' : self.cycle_id,
            'exam_schedules': self.exam_schedules
        }

class Mentor(db.Model):
    __tablename__ = 'mentors'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('pre_users.username'), unique=True, index=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    # ToDo - add column definitions

    mentees = db.relationship(Mentee.__name__)

    # ToDo - 1 mentor has 1 cycle
    cycle_id = db.Column(db.Integer, db.ForeignKey('cycles.id'))

class Meetings(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)
    # ToDo - add column definitions

    # ToDo - add relationship (A meeting takes place sometime between 1 mentor and 1 mentee)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'), nullable=False)
    mentor = db.relationship(Mentor.__name__, backref="meetings")

    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)
    mentee = db.relationship(Mentee.__name__, backref="meetings")


class Cycles(db.Model):
    __tablename__ = "cycles"

    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(50))
    cycle_start = db.Column(db.DateTime)
    cycle_end = db.Column(db.DateTime)
    region = db.Column(db.String(60)) #europe, americas

    mentees = db.relationship(Mentee.__name__)
    mentors = db.relationship(Mentor.__name__)


class User(UserMixin, db.Model):
    __tablename__ = "pre_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # Uploads
    uploads = db.relationship("Uploads")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username':self.username,
            'email':self.email,
            'password_hash':self.password_hash,
            'messages_sent': self.messages_sent,
        'messages_received': self.messages_received,
        'last_message_read_time': self.last_message_read_time
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

class University(db.Model):
    __tablename__ = "universities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country_iso_code = db.Column(db.String(3))

class Message(db.Model):

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('pre_users.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('pre_users.id'))

    #ToDo - add sender and recipient objects as relationships

    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)

class Exams(db.Model):
    __tablename__ = "exams"

    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(120))
    subcategory = db.Column(db.String(120))


class UniversityApplication(db.Model):
    __tablename__ = "university_applications"

    id = db.Column(db.Integer, primary_key=True)

    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)
    mentee = db.relationship(Mentee.__name__, backref="university_applications")

    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)
    university = db.relationship(University.__name__, backref="university_applications")


# ToDo - implement role class
#class Role(db.Model):
#    pass

class Uploads(db.Model):
    __tablename__ = "uploads"

    upload_id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(120), index=True, unique=True)
    # ToDo - add relationship to mentee and mentor
    username = db.Column(db.String(64), db.ForeignKey('pre_users.username'))


