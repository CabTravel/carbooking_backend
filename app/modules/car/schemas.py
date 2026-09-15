from pydantic import BaseModel, Field,ConfigDict
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

    model_config = ConfigDict(from_attributes=True)


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

    id: str
    localId: str
    carNumber: str
    carBrandName: str
    isAc: bool
    tripType: str
    seats: int
    driverName: str | None = None
    driverPhoneNumber: str | None = None

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


class CreateMultipleCarsParam(BaseModel):
    cars:list[CreateCarParam]

class CreateMultipleCarsOut(BaseModel):
    createdCars:list[CarResponseSchema]
    failedCars:list[CreateCarParam]
    reasons:list[str]

class UpdateMultipleCarsParam(BaseModel):
    cars:list[UpdateCarParam]

class UpdateMultipleCarsOut(BaseModel):
    updatedCars:list[CarResponseSchema]
    failedCars:list[UpdateCarParam]
    reasons:list[str]
    



class PatchCarParam(BaseModel):

    id: str

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
    localUpdateDate: int 

    coverImageUrl: str | None = None
    frontImageUrl: str | None = None
    backImageUrl: str | None = None
    leftImageUrl: str | None = None
    rightImageUrl: str | None = None


class OneCarOut(BaseModel):
    car: CarResponseSchema


class CarsListOut(BaseModel):
    cars: list[CarResponseSchema]


class CarSearchParam(BaseModel):
    fromStation:str|None=None
    toStation:str|None=None
    seats:int|None=None
    
