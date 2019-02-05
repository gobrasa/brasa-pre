# Flask settings
#FLASK_SERVER_NAME = 'localhost:8888'
import os

FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
#SQLALCHEMY_DATABASE_URI = "postgresql://localhost/brasa_pre5"
SQLALCHEMY_TRACK_MODIFICATIONS = False


DEBUG = False
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = 'this-really-needs-to-be-changed'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')