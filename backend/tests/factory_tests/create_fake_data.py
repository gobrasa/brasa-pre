from typing import List
import os
import sqlalchemy

from dotenv import load_dotenv

from backend.tests.factory_tests.fake_models import UserFactory, UniversityFactory
from models import University


def insert_entities(conn: sqlalchemy.engine.base.Connection, table: sqlalchemy.Table, entities: List) -> None:
    conn.execute(table.insert(), [i.__dict__ for i in users])

def create_local_postgres_engine(conn_string):
    return sqlalchemy.create_engine(conn_string)

if __name__ == "__main__":

    load_dotenv(dotenv_path='/Users/gabrielfior/brasa-pre/backend/src/.env', verbose=True)
    engine = create_local_postgres_engine(os.environ['HEROKU_DATABASE_URL'])
    meta = sqlalchemy.MetaData(bind=engine)

    users = UserFactory.build_batch(10)
    user_table = sqlalchemy.Table('pre_users', meta, autoload=True)

    univs = UniversityFactory.build_batch(10)
    univ_table = sqlalchemy.Table(University.__tablename__, meta, autoload=True)

    with engine.connect() as conn:
        # insert_entities(conn, user_table, [i.__dict__ for i in users])
        insert_entities(conn, univ_table, [i.__dict__ for i in univs])

