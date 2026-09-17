from time import time

from fastapi import Depends
import razorpay

from app.core.settings import get_settings
from app.modules.payment.repository import PaymentRepository
from sqlalchemy.dialects.postgresql import UUID
import hashlib
import hmac
from fastapi import HTTPException,status
import json
from app.modules.payment.schema import CreatePaymentOrderOut, CreatePaymentOrderParam

settings=get_settings()

class PaymentService:

    def __init__(
        self,
        repository: PaymentRepository = Depends()
    ):
        self.repository = repository

        self.razorpay = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

    async def create_payment_order(
        self,
        userId: UUID,
        param: CreatePaymentOrderParam
    ):

        plan = await self.repository.get_plan(
            planId=param.planId
        )

        receipt = f"subscription_{userId}_{int(time.time())}"

        order = await self.repository.create_order(
            userId=userId,
            planId=plan.id,
            amount=plan.amount,
            currency=plan.currency,
            receipt=receipt
        )

        razorpayOrder = self.razorpay.order.create({
            "amount": plan.amount,
            "currency": plan.currency,
            "receipt": receipt
        })

        await self.repository.update_razorpay_order(
            order=order,
            razorpayOrderId=razorpayOrder["id"]
        )

        return CreatePaymentOrderOut(
            orderId=order.id,
            razorpayOrderId=razorpayOrder["id"],
            amount=plan.amount,
            currency=plan.currency,
            keyId=settings.RAZORPAY_KEY_ID
        )


    def verify_webhook_signature(
        self,
        body: bytes,
        received_signature: str
    ) -> bool:

        expected_signature = hmac.new(
            settings.RAZORPAY_WEBHOOK_SECRET.encode(),
            body,
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(
            expected_signature,
            received_signature
        )

async def receive_webhook(
    self,
    body: bytes,
    signature: str,
    eventId: str
):

    # 1. Verify Razorpay signature

    is_valid = self.verify_webhook_signature(
        body=body,
        received_signature=signature
    )

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Razorpay webhook signature"
        )

    # 2. Parse only AFTER signature verification

    payload = json.loads(body)

    eventType = payload.get("event")

    # 3. Save webhook event

    webhookEvent = await self.repository.create_webhook_event(
        eventId=eventId,
        eventType=eventType,
        payload=payload
    )

    # 4. If duplicate, don't process again

    if webhookEvent is None:
        return {
            "received": True,
            "duplicate": True
        }

    # 5. Publish event to RabbitMQ

    await publish_payment_event(
        eventId=eventId
    )

    return {
        "received": True
    }