from flask import Flask, jsonify
from logging import DEBUG, INFO

import os
from dotenv import load_dotenv
from flask_restless import APIManager

from database import db
from models import Mentee, Mentor, Users, Cycles, Meetings


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

        db.create_all()

    @app.route('/')
    def index():
        return 'Hello from index!'

    return app


def register_models(app):
    manager = APIManager(app, flask_sqlalchemy_db=db)

    # ToDo - check options - patch many, insert bulk, pagination
    manager.create_api(Mentee, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Mentor, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Users, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Cycles, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Meetings, methods=['GET', 'POST', 'DELETE'])

def setup_database(app):
    pass


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
