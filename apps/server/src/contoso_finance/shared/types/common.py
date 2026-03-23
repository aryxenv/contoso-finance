"""Common types, enums, and base schemas used across domains."""

from enum import StrEnum
from typing import Generic, TypeVar

from pydantic import BaseModel


class Status(StrEnum):
    """Generic status enum for domain entities."""

    DRAFT = "draft"
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class CurrencyCode(StrEnum):
    """Supported currency codes."""

    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


class SortOrder(StrEnum):
    """Sort direction."""

    ASC = "asc"
    DESC = "desc"


T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated response wrapper."""

    items: list[T]
    total: int
    page: int
    page_size: int
    total_pages: int
