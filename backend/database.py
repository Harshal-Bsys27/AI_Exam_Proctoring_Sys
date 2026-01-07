"""Database configuration for the FastAPI backend.

Sets up a local SQLite database using SQLAlchemy. Provides the declarative
base, engine, and a session dependency for request handlers.
"""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./proctor.db"

# check_same_thread=False is required for SQLite when used with FastAPI/uvicorn
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Yield a SQLAlchemy session per request and ensure close on exit."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
