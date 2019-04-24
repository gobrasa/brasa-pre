import datetime

from database import db


class University(db.Model):
    __tablename__ = "universities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country_iso_code = db.Column(db.String(3))


class Exams(db.Model):
    __tablename__ = "exams"

    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(120))
    subcategory = db.Column(db.String(120))


class UniversityApplication(db.Model):
    __tablename__ = "university_applications"

    id = db.Column(db.Integer, primary_key=True)

    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)
    mentee = db.relationship("Mentee", back_populates="university_applications")

    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)
    university = db.relationship(University.__name__, backref="university_applications")

class UniversityAccepted(db.Model):
    __tablename__ = "university_acceptances"

    id = db.Column(db.Integer, primary_key=True)

    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)
    mentee = db.relationship("Mentee", back_populates="university_acceptances")

    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)
    university = db.relationship(University.__name__, backref="university_acceptances")

class Person:
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))


class Mentee(db.Model, Person):
    __tablename__ = 'mentees'

    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'))
    username = db.Column(db.String(64), db.ForeignKey('users.username'), unique=True, index=True)
    financial_aid = db.Column(db.Boolean, nullable=False)
    cycle_id = db.Column(db.Integer, db.ForeignKey('cycles.id'))

    primary_contact_username = db.Column(db.String(64), db.ForeignKey('users.username'))
    primary_contact = db.relationship("User",
                                   foreign_keys=[primary_contact_username]
                                   )


    # Exam schedule
    exam_schedules = db.relationship("ExamSchedule")
    university_applications = db.relationship("UniversityApplication",
                                              back_populates="mentee", uselist=True)
    university_acceptances = db.relationship("UniversityAccepted",
                                              back_populates="mentee", uselist=True)


class ExamSchedule(db.Model):
    __tablename__ = 'scheduled_exams'

    # 1 mentee, many exam schedules
    id = db.Column(db.Integer, primary_key=True)
    realization_date = db.Column(db.DateTime, nullable=False)
    mentee_id = db.Column(db.Integer, db.ForeignKey('mentees.id'), nullable=False)

    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'))
    exam = db.relationship("Exams")
    score = db.Column(db.String(20))  # Not sure whether score is A or 100


class Mentor(db.Model, Person):
    __tablename__ = 'mentors'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'), unique=True, index=True)


    mentees = db.relationship(Mentee.__name__)

    cycle_id = db.Column(db.Integer, db.ForeignKey('cycles.id'))
    cycle = db.relationship("Cycles", back_populates="mentors")

    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=True)
    university = db.relationship(University.__name__, backref="mentors")

    # ToDO - add course relationship (as major and minor) - differentiate between mentors_majors and mentors_minors
    major_course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    major = db.relationship("Courses",
                            foreign_keys = [major_course_id]
                            )

    second_major_course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    second_major = db.relationship("Courses",
                            foreign_keys=[second_major_course_id]
                            )

    minor_course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    minor = db.relationship("Courses",
                            foreign_keys=[minor_course_id]
                            )

    second_minor_course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    second_minor = db.relationship("Courses",
                            foreign_keys=[second_minor_course_id]
                            )

    user = db.relationship("User")

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
    role_name = db.Column(db.String(30), db.ForeignKey('role.role_name'))
    uploads = db.relationship("Uploads")


class Uploads(db.Model):
    __tablename__ = "uploads"

    title = db.Column(db.String(120))
    upload_id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'))

class Courses(db.Model):
    __tablename__ = "courses"

    # ToDo - add relationship to mentors (one-to-one, as major and minor) -  differentiate between mentors_majors and mentors_minors
    # https://github.com/fivethirtyeight/data/blob/master/college-majors/majors-list.csv

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=True)
    category = db.Column(db.String(200))
    #mentors_major = db.relationship(Mentor.__name__, back_populates='major', foreign_keys=[Mentor.major_course_id])
    #mentors_minor = db.relationship(Mentor.__name__, back_populates='minor', foreign_keys=[Mentor.minor_course_id])
