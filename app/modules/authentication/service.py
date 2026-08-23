
from app.modules.authentication. repository import AuthRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.authentication.schemas import GenerateOtpRequest,VerifyOtpParam,CreateProfileParam,UpdateProfileParam
from uuid import UUID
from app.modules.authentication.schemas import Profile

from fastapi import Depends

class AuthService:
    def __init__(self,repository:AuthRepository=Depends()):
        self.repository=repository


    async def generate_otp(self, param:GenerateOtpRequest):

        result=await self.repository.generate_otp(param=param)
        return result

    async def verify_otp(self, param:VerifyOtpParam):

        result=await self.repository.generate_otp(param=param)
        return result    
    
    async def create_profile(self, param:CreateProfileParam):

        result=await self.repository.create_profile(param=param)
        return result 

    async def update_profile(self, param:UpdateProfileParam,userId=UUID) -> Profile:

        result=await self.repository.create_profile(param=param,userId=userId)
        return result 
    
        




