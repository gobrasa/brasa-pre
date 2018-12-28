from flask import Flask, jsonify

import os
from dotenv import load_dotenv
from flask_restless import APIManager

from src.database import db
from flask_restful import Api
from src.ResultResource import ResultListResource, ResultResource
from src.models import Result


def create_app():

    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        blueprint = register_models_endpoints(app)
        app.register_blueprint(blueprint)

    #db.init_app(app)


    return app

def register_models_endpoints(app):
    manager = APIManager(app, flask_sqlalchemy_db=db)
    #manager.create_api(Result, methods=['GET', 'POST', 'DELETE'])
    blueprint = manager.create_api_blueprint(Result, methods=['GET', 'POST', 'DELETE'])
    return blueprint



def setup_database(app):
    pass

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
