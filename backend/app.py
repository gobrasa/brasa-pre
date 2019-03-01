import os

import flask
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restless import APIManager

import settings
from database import db
from database.models import Mentee, University, Mentor, User, Exams, ExamSchedule, Uploads, Message, Meetings
from endpoints.logic_for_endpoints import return_routes_for_logic_endpoints, EndpointLogicConfigurator

logic_config = EndpointLogicConfigurator()
models_for_endpoints = {Mentee, University, Mentor, User,
                        ExamSchedule, Exams, Uploads, Message,
                        Meetings}

def register_blueprints(app, max_results_per_page = 2000):

    manager = APIManager(app, flask_sqlalchemy_db=db)

    for model in models_for_endpoints:

        blueprint = manager.create_api_blueprint(
            model,
            methods=['GET','POST','PUT','DELETE'],
            results_per_page=0
            #preprocessors= cors_preprocessor
        )

        app.register_blueprint(blueprint)

def configure_logic_endpoints(app: flask.app, routes_for_endpoints = return_routes_for_logic_endpoints()):
    """

    :type app: flask.app
    """
    for url, methods, function in routes_for_endpoints:
        pass



def configure_app(flask_app):

    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') if not None else settings.SQLALCHEMY_DATABASE_URI


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app = logic_config.configure_logic_endpoints(app)

    return init_app(app)


def init_app(app):

    configure_app(app)
    configure_logic_endpoints(app)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)
        cors = CORS(app)



    return app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
