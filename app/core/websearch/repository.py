
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from fastapi import Depends
from app.database.session import get_db
from app.core.websearch.schema import CarSearchParam
from app.modules.car.repository import CarRepository
from app.modules.authentication.repository import AuthRepository


class WebRepository:

    def __init__(self,carRepo:CarRepository=Depends(),userRepo:AuthRepository=Depends()):
        self.carRepo=carRepo
        self.userRepo=userRepo

    async def search_cars(self, param:CarSearchParam):
        cars=await self.carRepo.search_cars(param=param)
        return cars

    async def get_one_profile(self,userId:UUID):
        user=await self.userRepo.get_user_with_cars(userId=userId)
        return user









        
