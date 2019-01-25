import datetime

from flask import Flask, jsonify, request
from logging import DEBUG, INFO

import os
from dotenv import load_dotenv
from flask_restless import APIManager

from database import db
from models import Mentee, Mentor, User, Cycles, Meetings, Message, University, Exams, UniversityApplication, \
    ExamSchedule, Uploads


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.logger.log(INFO, 'APP Settings : {}'.format(os.environ['APP_SETTINGS']))
    app.config.from_object(os.environ['APP_SETTINGS'])
    # ToDo - move SQLALCHEMY_TRACK_MODIFICATIONS to .env file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        register_models(app)


    @app.route('/')
    def index():
        return 'Hello from index!'
    #

    @app.route('/send_message/<sender>/<recipient>', methods=['GET', 'POST'])
    def send_message(sender, recipient):
        recipient = User.query.filter_by(username=recipient).first_or_404()
        sender = User.query.filter_by(username=sender).first_or_404()
        body = request.form
        msg = Message(author=sender, recipient=recipient,
                      body=body)
        db.session.add(msg)
        db.session.commit()
        print('Your message has been sent.')
        return msg.id

    @app.route('/<username>/messages')
    def messages(username):
        user = User.query.filter_by(username=username).first_or_404()
        user.last_message_read_time = datetime.datetime.utcnow()
        db.session.commit()
        messages = user.messages_received.order_by(
            Message.timestamp.desc())
        return messages

    return app


def register_models(app):
    manager = APIManager(app, flask_sqlalchemy_db=db)

    # ToDo - check options - patch many, insert bulk, pagination
    manager.create_api(Mentee, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Mentor, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(User, methods=['GET', 'POST', 'DELETE'], exclude_columns=['password_hash'])
    manager.create_api(Cycles, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Meetings, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(University, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Message, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Exams, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(ExamSchedule, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(UniversityApplication, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Uploads, methods=['GET', 'POST', 'DELETE'])

def setup_database(app):
    pass


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
