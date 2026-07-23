"""
Company model.
"""

from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base
from sqlalchemy.orm import relationship


class Company(Base):
    """Represents a company using the application."""

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    company_name: Mapped[str] = mapped_column(String(150), nullable=False)
    cabin_name: Mapped[str] = mapped_column(String(150), nullable=False)

    owner_name: Mapped[str] = mapped_column(String(150), nullable=False)

    phone: Mapped[str] = mapped_column(String(30), nullable=False)

    email: Mapped[str | None] = mapped_column(String(150), nullable=True)

    address: Mapped[str] = mapped_column(String(255), nullable=False)

    city: Mapped[str] = mapped_column(String(100), nullable=False)

    province: Mapped[str] = mapped_column(String(100), nullable=False)

    country: Mapped[str] = mapped_column(String(100), nullable=False)

    logo: Mapped[str | None] = mapped_column(String(255), nullable=True)

    main_currency: Mapped[str] = mapped_column(String(10), default="CDF")

    current_exchange_rate: Mapped[float] = mapped_column(Float, default=1.0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    operators = relationship(
    "Operator",
    back_populates="company",
    cascade="all, delete-orphan",
    )
    