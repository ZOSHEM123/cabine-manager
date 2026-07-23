"""
Company repository.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.company import Company
from repositories.base_repository import BaseRepository


class CompanyRepository(BaseRepository[Company]):
    """Repository dedicated to Company operations."""

    def __init__(self, session: Session) -> None:
        super().__init__(session, Company)

    def get_first_company(self) -> Company | None:
        """
        Return the first company stored in the database.
        """
        statement = select(Company).limit(1)
        return self.session.execute(statement).scalar_one_or_none()

    def exists(self) -> bool:
        """
        Check whether a company already exists.
        """
        return self.get_first_company() is not None