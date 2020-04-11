import pytest

from backend.app import create_app


@pytest.fixture
def app():
    app = create_app()
    app = configure_test_db(app)
    return app


def create_entities(db):
    # create users
    # create cycles
    # create mentors
    # create mentees
    pass


def configure_test_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    # TODO: Apply migrations on the fly to test.db from alembic versions
    from backend.database import db
    with app.app_context():
        db.create_all()
        create_entities(db)

    return app
