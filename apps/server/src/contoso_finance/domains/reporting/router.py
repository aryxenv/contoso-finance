"""Reporting domain API routes."""

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from contoso_finance.domains.reporting import service
from contoso_finance.domains.reporting.schemas import (
    DashboardMetrics,
    ReportListResponse,
    ReportRequest,
    ReportResponse,
)
from contoso_finance.shared.database.session import get_db

router = APIRouter(prefix="/api/reporting", tags=["reporting"])


@router.get("/reports", response_model=ReportListResponse)
async def list_reports(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
) -> ReportListResponse:
    return await service.list_reports(db, page, page_size)


@router.get("/reports/{report_id}", response_model=ReportResponse)
async def get_report(
    report_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> ReportResponse:
    return await service.get_report(db, report_id)


@router.post("/reports", response_model=ReportResponse, status_code=201)
async def generate_report(
    data: ReportRequest,
    db: AsyncSession = Depends(get_db),
) -> ReportResponse:
    return await service.generate_report(db, data)


@router.delete("/reports/{report_id}", status_code=204)
async def delete_report(
    report_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> None:
    await service.delete_report(db, report_id)


@router.get("/dashboard", response_model=DashboardMetrics)
async def get_dashboard_metrics(
    db: AsyncSession = Depends(get_db),
) -> DashboardMetrics:
    return await service.get_dashboard_metrics(db)
