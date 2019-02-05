import logging.config
import os

from dotenv import load_dotenv
from flask import Flask

import settings
from database import db
from restful_api.endpoints import api

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


def create_app():
    load_dotenv()
    app = Flask(__name__)
    api.init_app(app)

    return init_app(app)


def init_app(app):
    configure_app(app)

    with app.app_context():
        db.init_app(app)

    @app.route('/test')
    def index():
        return 'Hello from index!'

    return app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)