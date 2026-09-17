
from app.core.websearch.repository import WebRepository
from fastapi import Depends
from uuid import UUID
from app.core.websearch.schema import CarSearchParam,CarSearchResponse,OneCarForWeb,CarsSearchWebResponse,OneCompanyProfile
from app.modules.car.schemas import CarResponseSchema
from app.modules.authentication.schemas import OneFullUser
class WebService:


    def __init__(self,repository:WebRepository=Depends()):
        self.repository=repository

    async def search_cars(self,param:CarSearchParam):

        result=await self.repository.search_cars(param=param)

        

        # return result

        return CarsSearchWebResponse(cars= [OneCarForWeb(
        car=CarResponseSchema.model_validate(car),
        user=OneFullUser.model_validate(car.user)
             )
    for car in result] )

    async def get_one_profile(self,username=str):

        result=await self.repository.get_one_profile(username=username)

        return OneCompanyProfile(
            user= OneFullUser.model_validate(result),
            cars=  [CarResponseSchema.model_validate(car)
    for car in result.cars]
        )



    



        
