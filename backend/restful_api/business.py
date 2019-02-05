import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, check_password_hash

from restful_api.Exceptions import RoleNotAllowedException
from database import db
from database.models import User, Role, Mentee, Mentor, Uploads, Exams, ExamSchedule
from settings import SQLALCHEMY_DATABASE_URI


def create_user(data):
    username = data.get('username')
    email = data.get('email')
    role_name = data.get('role_name')

    user = User(username=username, email=email,
                role_name=role_name)
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

def check_role_name_valid(role_name):

    allowed_role_names = [i.role_name for i in Role.query.all()]

    if role_name not in allowed_role_names:
        raise RoleNotAllowedException('Not allowed role {}'.format(role_name),
                                      'Allowed roles: {}'.format(allowed_role_names))


def update_user(user_id, data):
    user = User.query.filter(User.id == user_id).one()
    user.username = data.get('username')
    user.email = data.get('email')
    user.role_name = data.get('role_name') if data.get('role_name') is not None else user.role_name

    check_role_name_valid(user.role_name)

    User.query.session.add(user)
    User.query.session.commit()


def delete_user(user_id):
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()

def create_mentee(data):

    mentor_id = data.get('mentor_id')
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    city = data.get('city')
    state = data.get('state')
    financial_aid = data.get('financial_aid')
    cycle_id = data.get('cycle_id')

    mentee = Mentee(mentor_id=mentor_id,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    city=city,
                    state=state,
                    financial_aid=financial_aid,
                    cycle_id=cycle_id)

    db.session.add(mentee)
    db.session.commit()

def create_upload(data):

    link = data.get('link')
    username = data.get('username')

    upload = Uploads(link=link,
                    username=username)

    db.session.add(upload)
    db.session.commit()

def create_exam(data):

    category = data.get('category')
    subcategory = data.get('subcategory')

    exam = Exams(category=category,
                    subcategory=subcategory)

    db.session.add(exam)
    db.session.commit()

def update_exam(id, data):
    exam = Exams.query.filter(Exams.id == id).one()

    exam.category = data.get('category')
    exam.subcategory = data.get('subcategory')

    Exams.query.session.add(exam)
    Exams.query.session.commit()


def create_exam_schedule(data):

    realization_date = data.get('realization_date')
    mentee_id = data.get('mentee_id')
    exam_id = data.get('exam_id')
    score = data.get('score')

    exam_schedule = ExamSchedule(realization_date=realization_date,
                                 mentee_id=mentee_id,
                                 exam_id=exam_id,
                                 score=score)

    db.session.add(exam_schedule)
    db.session.commit()

def update_exam_schedule(id, data):
    exam_schedule = ExamSchedule.query.filter(ExamSchedule.id == id).one()

    exam_schedule.realization_date = data.get('realization_date')
    exam_schedule.mentee_id = data.get('mentee_id')
    exam_schedule.exam_id = data.get('exam_id')
    exam_schedule.score = data.get('score')

    ExamSchedule.query.session.add(exam_schedule)
    ExamSchedule.query.session.commit()

def update_mentee(id, data):
    mentee = Mentee.query.filter(Mentee.id == id).one()

    mentee.mentor_id = data.get('mentor_id'),
    mentee.first_name = data.get('first_name'),
    mentee.last_name = data.get('last_name'),
    mentee.city = data.get('city'),
    mentee.state = data.get('state'),
    mentee.financial_aid = data.get('financial_aid'),
    mentee.cycle_id = data.get('cycle_id')

    Mentee.query.session.add(mentee)
    Mentee.query.session.commit()

def update_mentor(id, data):
    mentor = Mentor.query.filter(Mentor.id == id).one()

    mentor.first_name = data.get('first_name'),
    mentor.last_name = data.get('last_name'),
    mentor.cycle_id = data.get('cycle_id')

    Mentor.query.session.add(mentor)
    Mentor.query.session.commit()

def update_upload(id, data):
    upload = Uploads.query.filter(Uploads.id == id).one()

    upload.link = data.get('link')

    Uploads.query.session.add(upload)
    Uploads.query.session.commit()

def delete_from_table(class_var, id):
    db.session.query(class_var).filter(class_var.id == id).delete()
    db.session.commit()