import logging.config

import os
from flask import Flask, Blueprint

import settings
from api.endpoints.users import ns as blog_categories_namespace
from api.endpoints.mentees import ns as mentee_namespace
from api.endpoints.mentors import ns as mentor_namespace
from api.endpoints.uploads import ns as uploads_namespace
from api.endpoints.exam_schedules import ns as exam_schedules_namespace
from api.endpoints.exams import ns as exams_namespace
from api.restplus import api

from database import db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI if not None else settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_categories_namespace)
    api.add_namespace(mentee_namespace)
    api.add_namespace(mentor_namespace)
    api.add_namespace(uploads_namespace)
    api.add_namespace(exams_namespace)
    api.add_namespace(exam_schedules_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)

    #init_login_routes(app)


    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
