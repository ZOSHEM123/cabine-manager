"""
Register all SQLAlchemy models.

Import every model here so SQLAlchemy can configure
relationships correctly.
"""

from .company import Company
from .operator import Operator

__all__ = [
    "Company",
    "Operator",
]