"""
Database configuration.

This module initializes the SQLAlchemy engine, session factory,
and declarative base for the entire application.
"""
import models

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config.settings import DATABASE_URL


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)
def create_database() -> None:
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)