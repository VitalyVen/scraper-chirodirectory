import sqlalchemy
from configs.settings import DB
from models.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_session():
    engine_url = sqlalchemy.engine.url.URL(
        drivername=DB["dialect"],
        host=DB["host"],
        port=DB["port"],
        username=DB["username"],
        password=DB["password"],
        database=DB["db_name"],
        # query={'charset': 'utf8mb4'}
    )

    db_engine = create_engine(
        engine_url, encoding="utf-8", echo=False, pool_recycle=3600
    )

    Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = scoped_session(Session)
    return db_engine, session


db_engine, session = get_session()

# def create_backup_schema():
#     """
#     Create schema
#
#     """
Base.metadata.create_all(db_engine)
