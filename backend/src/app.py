from flask import Flask, jsonify
from logging import DEBUG, INFO

import os
from dotenv import load_dotenv
from flask_restless import APIManager

from database import db
from models import Result, ExampleModel


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

    return app


def register_models(app):
    manager = APIManager(app, flask_sqlalchemy_db=db)
    app.register_blueprint(manager.create_api_blueprint(Result, methods=['GET', 'POST', 'DELETE']))
    app.register_blueprint(manager.create_api_blueprint(ExampleModel, methods=['GET', 'POST', 'DELETE']))


def setup_database(app):
    pass


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
