import flask
import os
from auth.auth import AuthError, requires_auth
from database import db
from database.models import Mentee, University, Mentor, User, Exams, ExamSchedule, Uploads, \
    UniversityApplication, Courses, UniversityAccepted
from dotenv import load_dotenv
from endpoints.logic_for_endpoints import EndpointLogicConfigurator
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restless import APIManager

logic_config = EndpointLogicConfigurator()

# Models which will be exposed as endpoints (GET, POST, PUT, DELETE)
models_for_endpoints = {Mentee, University, Mentor, User,
                        ExamSchedule, Uploads,
                        UniversityApplication, Courses,
                        Exams, UniversityAccepted}


def register_blueprints(app):
    """ Registers blueprints and endpoints for tables in models to be exposed """
    manager = APIManager(app, flask_sqlalchemy_db=db)

    for model in models_for_endpoints:
        blueprint = manager.create_api_blueprint(
            model,
            methods=['GET', 'POST', 'PUT', 'DELETE'],
            results_per_page=0,
            preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func], POST=[auth_func],
                               PUT=[auth_func], DELETE=[auth_func])
        )

        app.register_blueprint(blueprint)


@requires_auth
def auth_func(*args, **kw):
    """ Function used as pre-processor for all endpoints so that authentication is required """
    print('entered auth_func')
    pass


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL') if not None else settings.SQLALCHEMY_DATABASE_URI


def register_error_handler(app):
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = flask.jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    @app.route('/private')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:5000"])
    @requires_auth
    def private():
        response = "Hello from a private endpoint! You need to be authenticated to see this."
        return flask.jsonify(message=response)


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app = logic_config.configure_logic_endpoints(app)

    return init_app(app)


def init_app(app):
    configure_app(app)

    with app.app_context():
        db.init_app(app)
        register_error_handler(app)
        register_blueprints(app)
        cors = CORS(app)

    return app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
