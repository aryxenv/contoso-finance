"""Pydantic v2 schemas for the billing domain."""

from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from contoso_finance.shared.types.common import CurrencyCode, PaginatedResponse, Status

# --- Line Item schemas ---


class LineItemCreate(BaseModel):
    """Schema for creating a line item."""

    description: str
    quantity: int
    unit_price: float


class LineItemResponse(BaseModel):
    """Schema for line item API responses."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    description: str
    quantity: int
    unit_price: Decimal
    total: Decimal


# --- Invoice schemas ---


class InvoiceCreate(BaseModel):
    """Schema for creating an invoice."""

    customer_name: str
    customer_email: str
    currency: CurrencyCode
    line_items: list[LineItemCreate]
    due_date: date


class InvoiceUpdate(BaseModel):
    """Schema for partially updating an invoice."""

    customer_name: str | None = None
    customer_email: str | None = None
    currency: CurrencyCode | None = None
    line_items: list[LineItemCreate] | None = None
    due_date: date | None = None


class InvoiceResponse(BaseModel):
    """Schema for invoice API responses."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    invoice_number: str
    customer_name: str
    customer_email: str
    status: Status
    currency: CurrencyCode
    subtotal: Decimal
    tax: Decimal
    total: Decimal
    due_date: date
    line_items: list[LineItemResponse]
    created_at: datetime
    updated_at: datetime


class InvoiceListResponse(PaginatedResponse[InvoiceResponse]):
    """Paginated list of invoices."""

    pass
