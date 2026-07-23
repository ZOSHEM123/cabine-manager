"""
Operator model.
"""

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Operator(Base):
    """Represents a telecom operator."""

    __tablename__ = "operators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
    )

    operator_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    alert_threshold: Mapped[float] = mapped_column(default=0.0)

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    company = relationship(
    "Company",
    back_populates="operators",
    )