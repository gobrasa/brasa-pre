import os
from app import app
from database import db
from dotenv import load_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

load_dotenv()

print(os.getenv('DATABASE_URL'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
