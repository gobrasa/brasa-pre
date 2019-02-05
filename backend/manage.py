import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import settings
from app import app, configure_app
from database import db
from dotenv import load_dotenv
load_dotenv()

#app.config.from_object(os.getenv('APP_SETTINGS'))
#initialize_app(app)
print (os.getenv('DATABASE_URL'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()