"""Pydantic v2 schemas for the Payments domain."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from contoso_finance.shared.types.common import CurrencyCode, PaginatedResponse


class PaymentMethodCreate(BaseModel):
    """Schema for creating a new payment method."""

    type: str
    last_four: str


class PaymentMethodResponse(BaseModel):
    """Schema for returning a payment method."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    type: str
    last_four: str
    is_default: bool


class PaymentCreate(BaseModel):
    """Schema for creating a new payment."""

    invoice_id: UUID | None = None
    amount: float
    currency: CurrencyCode
    payment_method_id: UUID


class PaymentResponse(BaseModel):
    """Schema for returning a payment."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    invoice_id: UUID | None
    amount: float
    currency: str
    status: str
    payment_method: PaymentMethodResponse
    reference: str
    created_at: datetime
    updated_at: datetime


class RefundRequest(BaseModel):
    """Schema for requesting a refund."""

    payment_id: UUID
    amount: float | None = None
    reason: str


class PaymentListResponse(PaginatedResponse[PaymentResponse]):
    """Paginated list of payments."""

    pass
