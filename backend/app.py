import logging.config
import os

from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_restful import Api

import settings
from api.endpoints.exam_schedules import ns as exam_schedules_namespace
from api.endpoints.exams import ns as exams_namespace
from api.endpoints.mentees import ns as mentee_namespace
from api.endpoints.mentors import ns as mentor_namespace
from api.endpoints.uploads import ns as uploads_namespace
from api.endpoints.users import ns as blog_categories_namespace
from api.restplus import api
from database import db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):

    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['CORS_HEADERS'] = 'Content-Type'

    DATABASE_URL = os.getenv('DATABASE_URL')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL if not None else settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def register_namespaces(api):

    api.add_namespace(blog_categories_namespace)
    api.add_namespace(mentee_namespace)
    api.add_namespace(mentor_namespace)
    api.add_namespace(uploads_namespace)
    api.add_namespace(exams_namespace)
    api.add_namespace(exam_schedules_namespace)

def create_app():
    load_dotenv()
    app = Flask(__name__)
    configure_app(app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    
    with app.app_context():
        db.init_app(app)
        register_namespaces(api)
        app.register_blueprint(blueprint)


    @app.route('/')
    def index():
        return 'Hello from index!'

    return app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)