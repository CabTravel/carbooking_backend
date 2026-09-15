
from app.modules.car.repository import CarRepository
from uuid import UUID
from app.modules.car. schemas import OneCarOut,CarsListOut,CreateCarParam,UpdateCarParam,PatchCarParam,CreateMultipleCarsParam,CreateMultipleCarsOut,UpdateMultipleCarsParam,UpdateMultipleCarsOut
from fastapi import Depends

class CarService:
    def __init__(self,repository:CarRepository=Depends()):
        self.repository=repository

    async def get_car_by_id(self,car_id:UUID,userId:UUID):
        result=await self.repository.get_car_by_id(carId=car_id)
        return OneCarOut(car=result)

    async def get_cars_of_user(self,userId:UUID):
        result=await self.repository.get_cars_by_user(userId=userId)
        return CarsListOut(cars=result)

    async def create_car(self,param:CreateCarParam,userId:UUID):
        result=await self.repository.create_car(param=param,userId=userId)
        return OneCarOut(car=result)

    async def update_car(self,param:UpdateCarParam,userId:UUID):
        result=await self.repository.update_car(param=param,userId=userId)
        return OneCarOut(car=result)

    async def patch_car(self,param:PatchCarParam,userId:UUID):
        result=await self.repository.patch_update_car(param=param,userId=userId)
        return OneCarOut(car=result)

    async def delete_car(self,carId:UUID,userId:UUID):
        result=await self.repository.delete_car(carId=carId,userId=userId)
        return OneCarOut(car=result)

    async def create_multiple_cars(self,userId:UUID,param:CreateMultipleCarsParam):

        result=await self.repository.create_multiple_cars(self,userId=userId,param=param)

        result= CreateMultipleCarsOut(createdCars=result[0],failedCars=result[1],reasons=result[2])

        return result

    async def update_multiple_cars(self,userId:UUID,param:UpdateMultipleCarsParam):

        result=await self.repository.update_multiple_cars(userId=userId,param=param)
        result= UpdateMultipleCarsOut(updatedCars=result[0],failedCars=result[1],reasons=result[2])
        return result

   




    

        