"""
Base repository.

Provides common CRUD operations for all repositories.
"""

from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from database.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Generic repository."""

    def __init__(self, session: Session, model: type[ModelType]) -> None:
        self.session = session
        self.model = model

    def create(self, entity: ModelType) -> ModelType:
        self.session.add(entity)
        self.session.flush()
        self.session.refresh(entity)
        return entity

    def get_by_id(self, entity_id: int) -> ModelType | None:
        return self.session.get(self.model, entity_id)

    def get_all(self) -> list[ModelType]:
        return self.session.query(self.model).all()

    def delete(self, entity: ModelType) -> None:
        self.session.delete(entity)