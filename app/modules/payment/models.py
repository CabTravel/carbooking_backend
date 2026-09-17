from app.database.session import Base


from app.core.database.remote_db_table_base_mixin import RemoteDbTableMixin
from sqlalchemy import (Column,String,Integer,BigInteger,Boolean,UniqueConstraint,ForeignKey,JSON)
from sqlalchemy.orm import (relationship)
from sqlalchemy.dialects.postgresql import UUID

class SubscriptionPlan(RemoteDbTableMixin, Base):
    __tablename__ = "subscriptionPlans"

    name = Column(String, nullable=False)

    durationMonths = Column(Integer, nullable=False)

    amount = Column(BigInteger, nullable=False)

    currency = Column(String(3), nullable=False, default="INR")

    isActive = Column(Boolean, nullable=False, default=True)


class PaymentOrder(RemoteDbTableMixin, Base):
    __tablename__ = "paymentOrders"

    __table_args__ = (
        UniqueConstraint(
            "razorpayOrderId",
            name="uq_payment_order_razorpay_order_id"
        ),
    )

    userId = Column(
        UUID,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    planId = Column(
        UUID,
        ForeignKey("subscriptionPlans.id"),
        nullable=False
    )

    amount = Column(BigInteger, nullable=False)

    currency = Column(
        String(3),
        nullable=False,
        default="INR"
    )

    status = Column(
        String,
        nullable=False,
        default="CREATED"
    )

    razorpayOrderId = Column(
        String,
        nullable=True,
        unique=True,
        index=True
    )

    receipt = Column(
        String,
        nullable=False,
        unique=True
    )

    user = relationship(
        "User",
        back_populates="paymentOrders"
    )

    plan = relationship(
        "SubscriptionPlan"
    )


class Payment(RemoteDbTableMixin, Base):

    __tablename__ = "payments"

    __table_args__ = (
        UniqueConstraint(
            "razorpayPaymentId",
            name="uq_payment_razorpay_payment_id"
        ),
    )

    userId = Column(
        UUID,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    orderId = Column(
        UUID,
        ForeignKey("paymentOrders.id"),
        nullable=False,
        index=True
    )

    amount = Column(
        BigInteger,
        nullable=False
    )

    currency = Column(
        String(3),
        nullable=False,
        default="INR"
    )

    razorpayPaymentId = Column(
        String,
        nullable=False,
        unique=True,
        index=True
    )

    razorpayOrderId = Column(
        String,
        nullable=False,
        index=True
    )

    status = Column(
        String,
        nullable=False
    )

    method = Column(
        String,
        nullable=True
    )

    rawResponse = Column(
        JSON,
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="payments"
    )

    order = relationship(
        "PaymentOrder"
    )



class Subscription(RemoteDbTableMixin, Base):
    __tablename__ = "subscriptions"

    userId = Column(
        UUID,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    paymentId = Column(
        UUID,
        ForeignKey("payments.id"),
        nullable=False,
        index=True
    )

    planId = Column(
        UUID,
        ForeignKey("subscriptionPlans.id"),
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="ACTIVE"
    )

    startDate = Column(
        BigInteger,
        nullable=False
    )

    endDate = Column(
        BigInteger,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="subscriptions"
    )

    payment = relationship(
        "Payment"
    )

    plan = relationship(
        "SubscriptionPlan"
    )

class PaymentWebhookEvent(RemoteDbTableMixin, Base):
    __tablename__ = "paymentWebhookEvents"

    eventId = Column(
        String,
        nullable=False,
        unique=True,
        index=True
    )

    eventType = Column(
        String,
        nullable=False
    )

    payload = Column(
        JSON,
        nullable=False
    )

    isProcessed = Column(
        Boolean,
        nullable=False,
        default=False
    )

    processedAt = Column(
        BigInteger,
        nullable=True
    )