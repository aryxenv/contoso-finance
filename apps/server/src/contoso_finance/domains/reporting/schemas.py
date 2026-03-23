"""Reporting domain Pydantic schemas."""

import uuid
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from contoso_finance.shared.types.common import CurrencyCode, PaginatedResponse


class MetricDataPointResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    label: str
    value: float


class ReportRequest(BaseModel):
    type: str
    period: str
    currency: CurrencyCode
    start_date: date
    end_date: date


class ReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    report_type: str
    period: str
    currency: CurrencyCode
    start_date: date
    end_date: date
    data_points: list[MetricDataPointResponse]
    generated_at: datetime
    created_at: datetime
    updated_at: datetime


class DashboardMetrics(BaseModel):
    total_revenue: float
    total_expenses: float
    net_income: float
    pending_invoices: int
    pending_payments: int
    currency: CurrencyCode
    period: str


class ReportListResponse(PaginatedResponse[ReportResponse]):
    pass
