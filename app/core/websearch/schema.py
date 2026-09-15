from pydantic import BaseModel
from app.modules.authentication.models import User
from app.modules.authentication.schemas import OneFullUser
from app.modules.car.schemas import CarResponseSchema

class CarSearchParam(BaseModel):
    fromLocation: str | None = None
    toLocation: str | None = None
    seats: int | None = None
    username: str | None = None
    companyName: str | None = None


class OneCarForWeb(BaseModel):
    car:CarResponseSchema
    user:OneFullUser

    

class CarsSearchWebResponse(BaseModel):
    cars:list[OneCarForWeb]


class OneCompanyProfile(BaseModel):
    user: OneFullUser
    cars: list[CarResponseSchema]


    @classmethod
    def transform_user(cls, value):

        # SQLAlchemy User object
        if isinstance(value, User):

            return {
                "user": OneFullUser.model_validate(value),
                "cars": [
                    CarResponseSchema.model_validate(car)
                    for car in value.cars
                ]
            }

        return value


class CarSearchResponse(BaseModel):
    companies:list[OneCompanyProfile]



