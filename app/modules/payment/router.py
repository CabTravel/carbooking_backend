from fastapi import APIRouter, Depends
from uuid import UUID

from app.core.server_response import SuccessResponse
from app.core.security import get_current_user_id
from fastapi import Request,Header
from app.modules.payment.service import PaymentService
from app.modules.payment.schema import (
    CreatePaymentOrderParam,
    VerifyPaymentParam
)

router = APIRouter(
    prefix="/payment"
)

@router.post(
    "/create-order",
    response_model=SuccessResponse
)
async def create_payment_order(
    param: CreatePaymentOrderParam,
    service: PaymentService = Depends(),
    userId: UUID = Depends(get_current_user_id)
):

    result = await service.create_payment_order(
        userId=userId,
        param=param
    )

    return SuccessResponse(
        data=result
    )


@router.post("/webhook")
async def razorpay_webhook(
    request: Request,
    service: PaymentService = Depends(),
    razorpay_signature: str = Header(
        alias="X-Razorpay-Signature"
    ),
    razorpay_event_id: str = Header(
        alias="x-razorpay-event-id"
    )
):

    body = await request.body()

    result = await service.receive_webhook(
        body=body,
        signature=razorpay_signature,
        eventId=razorpay_event_id
    )

    return result