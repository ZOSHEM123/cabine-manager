"""
Database session management.

Provides a reusable context manager for database sessions.
"""

from contextlib import contextmanager

from database.database import SessionLocal


@contextmanager
def get_session():
    """
    Provide a transactional database session.
    """

    session = SessionLocal()

    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()