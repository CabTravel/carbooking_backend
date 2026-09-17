from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends, HTTPException, status
from uuid import UUID

from app.database.session import get_db

from app.modules.payment.models import (
    SubscriptionPlan,
    PaymentOrder,
    Payment,
    Subscription,
    PaymentWebhookEvent
)


class PaymentRepository:

    def __init__(
        self,
        db: AsyncSession = Depends(get_db)
    ):
        self.db = db

    async def get_plan(
        self,
        planId: UUID
    ) -> SubscriptionPlan:

        result = await self.db.execute(
            select(SubscriptionPlan)
            .where(
                SubscriptionPlan.id == planId,
                SubscriptionPlan.isActive == True
            )
        )

        plan = result.scalar_one_or_none()

        if plan is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subscription plan not found"
            )

        return plan
    
    async def create_order(
        self,
        userId: UUID,
        planId: UUID,
        amount: int,
        currency: str,
        receipt: str
    ) -> PaymentOrder:

        order = PaymentOrder(
            userId=userId,
            planId=planId,
            amount=amount,
            currency=currency,
            status="CREATED",
            receipt=receipt
        )

        self.db.add(order)

        await self.db.commit()
        await self.db.refresh(order)

        return order

    async def update_razorpay_order(
        self,
        order: PaymentOrder,
        razorpayOrderId: str
    ) -> PaymentOrder:

        order.razorpayOrderId = razorpayOrderId
        order.status = "PAYMENT_PENDING"

        await self.db.commit()
        await self.db.refresh(order)

        return order

    async def get_order(
        self,
        orderId: UUID,
        userId: UUID
        ) -> PaymentOrder:

        result = await self.db.execute(
            select(PaymentOrder)
            .where(
                PaymentOrder.id == orderId,
                PaymentOrder.userId == userId
            )
        )

        order = result.scalar_one_or_none()

        if order is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment order not found"
            )

        return order

    async def get_order_by_razorpay_id(
        self,
        razorpayOrderId: str
    ) -> PaymentOrder:

        result = await self.db.execute(
            select(PaymentOrder)
            .where(
                PaymentOrder.razorpayOrderId == razorpayOrderId
            )
        )

        order = result.scalar_one_or_none()

        if order is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment order not found"
            )

        return order


    async def create_payment(
        self,
        userId: UUID,
        orderId: UUID,
        razorpayPaymentId: str,
        razorpayOrderId: str,
        amount: int,
        currency: str,
        statusValue: str,
        method: str | None,
        rawResponse: dict
    ) -> Payment:

        payment = Payment(
            userId=userId,
            orderId=orderId,
            razorpayPaymentId=razorpayPaymentId,
            razorpayOrderId=razorpayOrderId,
            amount=amount,
            currency=currency,
            status=statusValue,
            method=method,
            rawResponse=rawResponse
        )

        self.db.add(payment)

        await self.db.commit()
        await self.db.refresh(payment)

        return payment

    async def create_subscription(
        self,
        userId: UUID,
        paymentId: UUID,
        planId: UUID,
        startDate: int,
        endDate: int
        ) -> Subscription:

        subscription = Subscription(
            userId=userId,
            paymentId=paymentId,
            planId=planId,
            status="ACTIVE",
            startDate=startDate,
            endDate=endDate
        )

        self.db.add(subscription)

        await self.db.commit()
        await self.db.refresh(subscription)

        return subscription

async def create_webhook_event(
    self,
    eventId: str,
    eventType: str,
    payload: dict
):

    existing = await self.db.execute(
        select(PaymentWebhookEvent)
        .where(
            PaymentWebhookEvent.eventId == eventId
        )
    )

    existingEvent = existing.scalar_one_or_none()

    if existingEvent:
        return None

    event = PaymentWebhookEvent(
        eventId=eventId,
        eventType=eventType,
        payload=payload,
        isProcessed=False
    )

    self.db.add(event)

    await self.db.commit()
    await self.db.refresh(event)

    return event