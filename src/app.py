from flask import Flask, jsonify

import os
from dotenv import load_dotenv
from src.database import db
from flask_restful import Api
from src.ResultResource import ResultListResource, ResultResource

def create_app():

    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    register_endpoints(app)

    return app

def register_endpoints(app):
    # Flask restful
    api = Api(app)
    api.add_resource(ResultListResource, '/results')
    api.add_resource(ResultResource, '/results/<result_id>')

def setup_database(app):
    pass

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
