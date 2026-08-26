from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.car. models import Car
from sqlalchemy import select
from fastapi import HTTPException,status,Depends
from app.modules.car.schemas import UpdateCarParam,PatchCarParam,CreateCarParam
from app.database.session import get_db
from uuid import UUID

class CarRepository:
    def __init__(self,db:AsyncSession=Depends(get_db)):
        self.db=db

    async def get_car_by_id(self,carId:UUID) -> Car:
        result=await self.db.execute(select(Car).where(Car.id==carId))
        car =result.scalar_one_or_none()
        if car is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No car exist with id')
        return car

    async def get_cars_by_user(self,userId:UUID)-> list[Car]:
        result=await self.db.execute(select(Car).where(Car.userId==userId))

        myList=result.scalars().all()

        return myList

    async def create_car(self,param:CreateCarParam,userId:UUID)-> Car: 
        car= Car(
           
            localId=param.localId,
            carNumber= param.carNumber,
            carBrandName=param.carBrandName,
            isAc=param.isAc,
            tripType=param.tripType,
            seats=param.seats,
            userId=userId,

            driverName=param.driverName,
            driverphoneNumber=param.driverphoneNumber,
            withDriverPerKmPrice=param.withDriverPerKmPrice,
            withDriverPerDayPrice=param.withDriverPerDayPrice,
            withoutDriverPerKmPrice=param.withoutDriverPerKmPrice,
            withoutDriverPerDayPrice=param.withoutDriverPerDayPrice,

            localCreateDate=param.localCreateDate,
            localUpdateDate=param.localUpdateDate,
            # Required
            coverImageUrl =param.coverImageUrl,
            frontImageUrl =param.frontImageUrl,
            backImageUrl =param.backImageUrl,
            leftImageUrl =param.leftImageUrl,
            rightImageUrl =param.rightImageUrl
              )

        self.db.add(car)
        await self.db.commit()
        await self.db.refresh(car)

        return car


    async def update_car(self,param:UpdateCarParam,userId=UUID):

        car=await self.get_car_by_id(carId=param.id)

        if car is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No car exist with id')

        if car.userId!=userId:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not autorised to edit")
   
        car.carNumber= param.carNumber
        car.carBrandName=param.carBrandName
        car.isAc=param.isAc
        car.tripType=param.tripType
        car.seats=param.seats
        
        car.driverName=param.driverName
        car.driverphoneNumber=param.driverphoneNumber
        car.withDriverPerKmPrice=param.withDriverPerKmPrice
        car.withDriverPerDayPrice=param.withDriverPerDayPrice
        car.withoutDriverPerKmPrice=param.withoutDriverPerKmPrice
        car.withoutDriverPerDayPrice=param.withoutDriverPerDayPrice
        
        car.localCreateDate=param.localCreateDate
        car.localUpdateDate=param.localUpdateDate
        # Required
        car.coverImageUrl =param.coverImageUrl
        car.frontImageUrl =param.frontImageUrl
        car.backImageUrl =param.backImageUrl
        car.leftImageUrl =param.leftImageUrl
        car.rightImageUrl =param.rightImageUrl

        await self.db.commit()
        await self.db.refresh(car)

        return car


    async def patch_update_car(self,param:PatchCarParam,userId:UUID):

        car= await self.get_car_by_id(carId=param.id)

        if car is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No car exist with id')

        if car.userId!=userId:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not autorised to edit")
   
        data= param.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(car,field,value)

        await self.db.commit()
        await self.db.refresh(car)

        return car



    async def delete_car(self,carId:UUID,userId:UUID):
        car=await self.get_car_by_id(carId=carId)

        if car is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No car exist with id')

        if car.userId!=userId:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='you are not authorized to delete')

        await self.db.delete(car)
        await self.db.commit()

        return car









        



        