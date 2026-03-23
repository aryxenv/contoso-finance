"""Pydantic schemas for the settlements domain."""

from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from contoso_finance.shared.types.common import CurrencyCode, PaginatedResponse


class SettlementItemResponse(BaseModel):
    """Response schema for a single settlement item."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    payment_id: UUID
    amount: Decimal
    fee: Decimal
    net_amount: Decimal


class SettlementCreate(BaseModel):
    """Request schema for creating a new settlement."""

    payment_ids: list[UUID]
    currency: CurrencyCode
    settlement_date: date


class SettlementResponse(BaseModel):
    """Response schema for a settlement."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    settlement_number: str
    status: str
    currency: str
    items: list[SettlementItemResponse]
    total_amount: Decimal
    total_fees: Decimal
    net_amount: Decimal
    settlement_date: date
    created_at: datetime
    updated_at: datetime


class SettlementListResponse(PaginatedResponse[SettlementResponse]):
    """Paginated list of settlements."""

    pass
