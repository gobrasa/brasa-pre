import logging.config
import os
import pandas as pd

import flask
import sqlalchemy
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine

import settings
from auth.auth import requires_role, AuthError, requires_auth
from database import db
from restful_api.endpoints import api
from restful_api.marsh import ma

app = Flask(__name__)

CORS(app, supports_credentials=True)

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

logging.getLogger('flask_cors').level = logging.DEBUG


def configure_app(flask_app):

    print('entered configure_app')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['CORS_HEADERS'] = 'Content-Type'

    DATABASE_URL = os.getenv('DATABASE_URL')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL if not None else settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def create_app():
    load_dotenv()
    app = Flask(__name__)
    api.init_app(app)
    register_error_handler(api)

    return init_app(app)


def init_app(app):
    configure_app(app)
    add_routes_manually(app)

    with app.app_context():
        db.init_app(app)
        #cors = CORS(app, resources={r"*": {"origins": "*"}})
        ma.init_app(app)

    return app

def add_routes_manually(flask_app):

    @flask_app.route('/exams2')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth
    def index():
        engine = create_engine('postgresql://localhost:5432/brasa_pre5')
        return flask.jsonify(pd.read_sql_table('exams', engine).to_dict(orient='records'))

    @flask_app.after_request  # blueprint can also be app~~
    def after_request(response):
        # response.headers['Access-Control-Allow-Origin'] = '*'
        # return response
        print('entered after request3')
        print(request)
        r = request.referrer[:-1] if request.referrer else 'http://localhost:4200'

        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,authorization')
        response.headers.add("Access-Control-Allow-Headers",
                             "Origin, X-Requested-With, Content-Type, Accept, authorization");
        response.headers.add('Access-Control-Allow-Methods', 'GET,HEAD,POST,OPTIONS,PUT,DELETE')
        response.headers.add('Access-Control-Allow-Credentials', 'true')

        return response


def register_error_handler(restful_api):

    @restful_api.errorhandler(AuthError)
    def handle_auth_error(ex):
        return {'message': ex.error}, ex.status_code

    @restful_api.errorhandler(sqlalchemy.orm.exc.NoResultFound)
    def handle_no_result_found(ex):
        print('entered handle_no_result')
        return {'message': str(ex)}, 404

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
