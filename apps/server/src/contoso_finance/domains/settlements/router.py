"""FastAPI router for the settlements domain."""

from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from contoso_finance.domains.settlements import service
from contoso_finance.domains.settlements.schemas import (
    SettlementCreate,
    SettlementListResponse,
    SettlementResponse,
)
from contoso_finance.shared.database.session import get_db

router = APIRouter(prefix="/api/settlements", tags=["settlements"])


@router.get("/", response_model=SettlementListResponse)
async def list_settlements(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
) -> SettlementListResponse:
    """List all settlements with pagination."""
    return await service.list_settlements(db, page, page_size)


@router.get("/{settlement_id}", response_model=SettlementResponse)
async def get_settlement(
    settlement_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> SettlementResponse:
    """Get a single settlement by ID."""
    return await service.get_settlement(db, settlement_id)


@router.post("/", response_model=SettlementResponse, status_code=201)
async def create_settlement(
    data: SettlementCreate,
    db: AsyncSession = Depends(get_db),
) -> SettlementResponse:
    """Create a new settlement."""
    return await service.create_settlement(db, data)


@router.post("/{settlement_id}/reconcile", response_model=SettlementResponse)
async def reconcile_settlement(
    settlement_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> SettlementResponse:
    """Start reconciliation for a settlement."""
    return await service.reconcile_settlement(db, settlement_id)


@router.post("/{settlement_id}/approve", response_model=SettlementResponse)
async def approve_settlement(
    settlement_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> SettlementResponse:
    """Approve a settlement."""
    return await service.approve_settlement(db, settlement_id)


@router.post("/{settlement_id}/complete", response_model=SettlementResponse)
async def complete_settlement(
    settlement_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> SettlementResponse:
    """Complete a settlement."""
    return await service.complete_settlement(db, settlement_id)


@router.delete("/{settlement_id}", status_code=204)
async def delete_settlement(
    settlement_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> None:
    """Delete a settlement."""
    from contoso_finance.domains.settlements import repository
    from contoso_finance.shared.middleware.error_handler import NotFoundError

    success = await repository.delete_settlement(db, settlement_id)
    if not success:
        raise NotFoundError(f"Settlement {settlement_id} not found")
