"""FastAPI router for the Payments domain."""

from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from contoso_finance.domains.payments import service
from contoso_finance.domains.payments.schemas import (
    PaymentCreate,
    PaymentListResponse,
    PaymentMethodCreate,
    PaymentMethodResponse,
    PaymentResponse,
    RefundRequest,
)
from contoso_finance.shared.database.session import get_db

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.get("/", response_model=PaymentListResponse)
async def list_payments(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List all payments with pagination."""
    return await service.list_payments(db, page, page_size)


@router.get("/methods", response_model=list[PaymentMethodResponse])
async def list_payment_methods(db: AsyncSession = Depends(get_db)):
    """List all payment methods."""
    return await service.list_payment_methods(db)


@router.post("/methods", response_model=PaymentMethodResponse, status_code=201)
async def create_payment_method(
    data: PaymentMethodCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new payment method."""
    return await service.create_payment_method(db, data)


@router.get("/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get a specific payment by ID."""
    return await service.get_payment(db, payment_id)


@router.post("/", response_model=PaymentResponse, status_code=201)
async def process_payment(
    data: PaymentCreate,
    db: AsyncSession = Depends(get_db),
):
    """Process a new payment."""
    return await service.process_payment(db, data)


@router.post("/{payment_id}/refund", response_model=PaymentResponse)
async def refund_payment(
    payment_id: UUID,
    refund: RefundRequest,
    db: AsyncSession = Depends(get_db),
):
    """Refund a completed payment."""
    return await service.refund_payment(db, payment_id, refund)
