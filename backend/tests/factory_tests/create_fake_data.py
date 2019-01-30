from typing import List
import os
import sqlalchemy

from dotenv import load_dotenv

from backend.tests.factory_tests.fake_models import UserFactory


def insert_entities(conn: sqlalchemy.engine.base.Connection, table: sqlalchemy.Table, entities: List) -> None:
    conn.execute(table.insert(), [i.__dict__ for i in entities])

def create_local_postgres_engine(conn_string):
    return sqlalchemy.create_engine(conn_string)

def load_local_dot_env():
    load_dotenv(dotenv_path='/Users/gabrielfior/brasa-pre/backend/src/.env', verbose=True)

if __name__ == "__main__":

    load_local_dot_env()
    #engine = create_local_postgres_engine(os.environ['HEROKU_DATABASE_URL'])
    engine = create_local_postgres_engine(os.environ['DATABASE_URL'])
    meta = sqlalchemy.MetaData(bind=engine)

    users = UserFactory.build_batch(10)
    user_table = sqlalchemy.Table('pre_users', meta, autoload=True)

    with engine.connect() as conn:
        insert_entities(conn, user_table, users)

