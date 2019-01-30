import datetime

import flask
import flask_restless
from flask import Flask, jsonify, request, after_this_request
from logging import DEBUG, INFO
import os
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from flask_restless import APIManager
import distutils

from flask_restless.views import ValidationError
from werkzeug.security import generate_password_hash

from database import db
from models import Mentee, Mentor, User, Cycles, Meetings, Message, University, Exams, UniversityApplication, \
    ExamSchedule, Uploads


def create_app():
    load_dotenv()
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
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

    @app.route('/register_mentee', methods= ['POST'])
    def register_mentee():
        # print form
        print(request.is_json)
        posted_json = request.get_json()

        # create mentee
        new_mentee = Mentee(username=posted_json.get('username'),
                            financial_aid=posted_json.get('financial_aid'),
                            mentor_id=posted_json.get('mentor_id'),
                            first_name=posted_json.get('first_name'),
                            last_name=posted_json.get('last_name'),
                            city=posted_json.get('city'),
                            state=posted_json.get('state'),
                            cycle_id=posted_json.get('cycle_id'),
                            )

        db.session.add(new_mentee)
        db.session.commit()

        return jsonify(new_mentee.serialize), 201

    @app.route("/cors", methods=['GET','POST'])
    @cross_origin()
    def cors_endpoint():
        return "Hello, cross-origin-world!"

    @app.route("/check_user_exists/<username>", methods=['GET'])
    def check_username_exists(username):
        users = User.query.filter_by(username=username).first_or_404()
        print (users)
        return '',200

    return app


def set_password_hash(**kwargs):
    pw = request.get_json()['password']
    request.get_json()['password_hash'] = generate_password_hash(pw)
    print ('finished set password hash')

def register_models(app):
    manager = APIManager(app, flask_sqlalchemy_db=db)

    # ToDo - check options - patch many, insert bulk, pagination
    manager.create_api(Mentee, methods=['GET', 'POST', 'DELETE'], preprocessors={'POST_RESOURCE':[allow_control_headers],
                                                                                 'GET_COLLECTION':[allow_control_headers]})
    manager.create_api(Mentor, methods=['GET', 'POST', 'DELETE'],
                       validation_exceptions=[ValidationError])

    user_preprocessor = {'POST': [set_password_hash]}
    manager.create_api(User, methods=['GET', 'POST', 'DELETE'], exclude_columns=['password_hash'], preprocessors=user_preprocessor)

    manager.create_api(Cycles, methods=['GET', 'POST', 'DELETE'],
                       validation_exceptions=[ValidationError])
    manager.create_api(Meetings, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(University, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Message, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Exams, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(ExamSchedule, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(UniversityApplication, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Uploads, methods=['GET', 'POST', 'DELETE'])

def setup_database(app):
    pass


def allow_control_headers(**kw):

    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
