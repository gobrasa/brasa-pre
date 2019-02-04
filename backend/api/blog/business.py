import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, check_password_hash

from api.Exceptions import RoleNotAllowedException
from database import db
from database.models import User, Role, Mentee
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

def update_mentee(id, data):
    mentee = Mentee.query.filter(Mentee.id == id).one()

    mentor_id = data.get('mentor_id'),
    username = data.get('username'),
    first_name = data.get('first_name'),
    last_name = data.get('last_name'),
    city = data.get('city'),
    state = data.get('state'),
    financial_aid = data.get('financial_aid'),
    cycle_id = data.get('cycle_id')

    Mentee.query.session.add(mentee)
    Mentee.query.session.commit()


def delete_from_table(class_var, id):
    db.session.query(class_var).filter(class_var.id == id).delete()
    db.session.commit()