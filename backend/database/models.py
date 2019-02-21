# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from restful_api.marsh import ma


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
    username = db.Column(db.String(64), db.ForeignKey('users.username'), unique=True, index=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    financial_aid = db.Column(db.Boolean, nullable=False)
    cycle_id = db.Column(db.Integer, db.ForeignKey('cycles.id'))

    # Exam schedule
    exam_schedules = db.relationship("ExamSchedule")

    university_applications = db.relationship("UniversityApplication",
                                              back_populates="mentee", uselist=True)

class MenteeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'mentor_id', 'username',
                  'first_name','last_name','city',
                  'state', 'financial_aid',
                  'cycle_id',
                  #'exam_schedules',
            #'university_applications'
)



class Mentor(db.Model):
    __tablename__ = 'mentors'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'), unique=True, index=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    mentees = db.relationship(Mentee.__name__)

    cycle_id = db.Column(db.Integer, db.ForeignKey('cycles.id'))
    cycle = db.relationship("Cycles", back_populates="mentors")


class Meetings(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)

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
    region = db.Column(db.String(60))  # europe, americas

    mentees = db.relationship(Mentee.__name__)
    mentors = db.relationship(Mentor.__name__, back_populates='cycle')


class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(30), unique=True)
    users = db.relationship("User")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String)
    role_name = db.Column(db.String(30), db.ForeignKey('role.role_name'))
    uploads = db.relationship("Uploads")
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email


    def set_password(self, secret):
        self.password_hash = generate_password_hash(secret)

    def check_password(self, secret):
        return check_password_hash(self.password_hash, secret)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email','role_name')


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
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)


class Exams(db.Model):
    __tablename__ = "exams"

    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(120))
    subcategory = db.Column(db.String(120))

class ExamsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'category', 'subcategory')
    # Smart hyperlinking


class UniversityApplication(db.Model):
    __tablename__ = "university_applications"

    id = db.Column(db.Integer, primary_key=True)

    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)
    mentee = db.relationship(Mentee.__name__, back_populates="university_applications")

    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)
    university = db.relationship(University.__name__, backref="university_applications")


class Uploads(db.Model):
    __tablename__ = "uploads"

    upload_id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'))

