import logging.config
import os

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

import settings
from auth.auth import requires_role, AuthError, requires_auth
from database import db
from restful_api.endpoints import api
from restful_api.marsh import ma

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.after_request
def after_request(response):

    print('entered after request')
    r = request.referrer[:-1]
    print(request.__dict__)

    response.headers.add('Access-Control-Allow-Origin', r)
    #response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200/')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

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


    @flask_app.route('/test')
    @requires_auth
    def index():
        return 'Hello from index!'


    @flask_app.route('/test-role')
    @requires_role('admin')
    def test_role():
        print('entered test role')
        return 'oi'


    @flask_app.after_request  # blueprint can also be app~~
    def after_request(response):
        print('entered after request')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response


    # @flask_app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Origin', '*')


def register_error_handler(restful_api):

    @restful_api.errorhandler(AuthError)
    def handle_auth_error(ex):
        return {'message': ex.error}, ex.status_code


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
