from pydantic import BaseModel, Field
from uuid import UUID


class CarResponseSchema(BaseModel):
    id: UUID

    localId: str
    carNumber: str
    carBrandName: str
    isAc: bool
    tripType: str
    seats: int

    driverName: str | None = None
    driverphoneNumber: str | None = None

    withDriverPerKmPrice: float | None = None
    withDriverPerDayPrice: float | None = None
    withoutDriverPerKmPrice: float | None = None
    withoutDriverPerDayPrice: float | None = None

    localCreateDate: int
    localUpdateDate: int
    createDate:int
    updateDate:int

    coverImageUrl: str | None = None
    frontImageUrl: str | None = None
    backImageUrl: str | None = None
    leftImageUrl: str | None = None
    rightImageUrl: str | None = None

    class Config:
        orm_mode = True


class CreateCarParam(BaseModel):

    localId: str

    carNumber: str
    carBrandName: str
    isAc: bool
    tripType: str
    seats: int
    driverName: str | None = None
    driverphoneNumber: str | None = None

    withDriverPerKmPrice: float | None = None
    withDriverPerDayPrice: float | None = None

    withoutDriverPerKmPrice: float | None = None
    withoutDriverPerDayPrice: float | None = None

    localCreateDate: int
    localUpdateDate: int

    coverImageUrl: str | None = None
    frontImageUrl: str | None = None
    backImageUrl: str | None = None
    leftImageUrl: str | None = None
    rightImageUrl: str | None = None


class UpdateCarParam(BaseModel):

    id: UUID
    localId: str
    carNumber: str
    carBrandName: str
    isAc: bool
    tripType: str
    seats: int
    driverName: str | None = None
    driverphoneNumber: str | None = None

    withDriverPerKmPrice: float | None = None
    withDriverPerDayPrice: float | None = None
    withoutDriverPerKmPrice: float | None = None
    withoutDriverPerDayPrice: float | None = None
    localCreateDate: int
    localUpdateDate: int

    coverImageUrl: str | None = None
    frontImageUrl: str | None = None
    backImageUrl: str | None = None
    leftImageUrl: str | None = None
    rightImageUrl: str | None = None


class PatchCarParam(BaseModel):

    id: UUID

    localId: str | None = None

    carNumber: str | None = None
    carBrandName: str | None = None
    isAc: bool | None = None
    tripType: str | None = None
    seats: int | None = None
    driverName: str | None = None
    driverphoneNumber: str | None = None
    withDriverPerKmPrice: float | None = None
    withDriverPerDayPrice: float | None = None
    withoutDriverPerKmPrice: float | None = None
    withoutDriverPerDayPrice: float | None = None
    localCreateDate: int | None = None
    localUpdateDate: int | None = None

    coverImageUrl: str | None = None
    frontImageUrl: str | None = None
    backImageUrl: str | None = None
    leftImageUrl: str | None = None
    rightImageUrl: str | None = None


class OneCarOut(BaseModel):
    car: CarResponseSchema


class CarsListOut(BaseModel):
    cars: list[CarResponseSchema]