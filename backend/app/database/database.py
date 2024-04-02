from typing import Any, Generator
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy_utils import create_database, database_exists

SQLALCHEMY_SQLLITE_DATABASE_URL = "sqlite:///app/database/park_pal_db.sqlite"

engine = create_engine(
    SQLALCHEMY_SQLLITE_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    if not database_exists(engine.url):
        create_database(engine.url)
    try:
        yield db
    finally:
        db.close()
        
class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )