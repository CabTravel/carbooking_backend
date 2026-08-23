from pydantic import BaseModel, Field
from uuid import UUID

class BookingResponseSchema(BaseModel):

    id: UUID
    localId: str
    carName: str
    carNumber: str
    customerName: str
    customerPhoneNumber: str = Field( min_length=10, max_length=10, pattern=r"^[0-9]{10}$",)
    amount: float
    bookingDate: int
    fromStation: str
    toStation: str
    notes: str | None = None
    carLocalId: str | None = None
    localCreateDate: int
    localUpdateDate: int
    createDate:int
    updateDate:int

    class Config:
        orm_mode = True

class CreateBookingParam(BaseModel):

    localId: str
    carName: str
    carNumber: str
    customerName: str
    customerPhoneNumber: str = Field( min_length=10, max_length=10, pattern=r"^[0-9]{10}$",)
    amount: float
    bookingDate: int
    fromStation: str
    toStation: str
    notes: str | None = None
    carLocalId: str | None = None
    localCreateDate: int
    localUpdateDate: int
    createDate:int
    updateDate:int


class UpdateBookingParam(BaseModel):

    id: UUID
    localId: str
    carName: str
    carNumber: str
    customerName: str
    customerPhoneNumber: str = Field( min_length=10, max_length=10, pattern=r"^[0-9]{10}$", )
    amount: float
    bookingDate: int
    fromStation: str
    toStation: str
    notes: str | None = None
    carLocalId: str | None = None
    localUpdateDate: int

class PatchBookingParam(BaseModel):

    id: UUID
    localId: str 
    carName: str | None = None
    carNumber: str | None = None
    customerName: str | None = None
    customerPhoneNumber: str | None = Field(default=None,  min_length=10,  max_length=10,  pattern=r"^[0-9]{10}$", )
    amount: float | None = None
    bookingDate: int | None = None
    fromStation: str | None = None
    toStation: str | None = None
    notes: str | None = None
    carLocalId: str | None = None
    localUpdateDate: int 




class OneBookingOut(BaseModel):
    booking: BookingResponseSchema


class BookingsListOut(BaseModel):
    bookings: list[BookingResponseSchema]