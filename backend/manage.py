import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, initialize_app
from database import db
from dotenv import load_dotenv
load_dotenv()

#app.config.from_object(os.getenv('APP_SETTINGS'))
initialize_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()