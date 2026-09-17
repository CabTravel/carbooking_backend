
from pydantic import BaseModel
from uuid import UUID


class CreatePaymentOrderParam(BaseModel):
    planId: UUID

class CreatePaymentOrderOut(BaseModel):
    orderId: UUID
    razorpayOrderId: str
    amount: int
    currency: str
    keyId: str

class VerifyPaymentParam(BaseModel):
    razorpayPaymentId: str
    razorpayOrderId: str
    razorpaySignature: str

class SubscriptionOut(BaseModel):
    id: UUID
    planId: UUID
    status: str
    startDate: int
    endDate: int