
from app.modules.authentication. repository import AuthRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.authentication.schemas import GenerateOtpRequest,VerifyOtpParam,CreateProfileParam,UpdateProfileParam
from uuid import UUID
from app.modules.authentication.schemas import Profile,GenerateOtpResponse,OneProfileOut

from fastapi import Depends

class AuthService:
    def __init__(self,repository:AuthRepository=Depends()):
        self.repository=repository


    async def generate_otp(self, param:GenerateOtpRequest):

        result=await self.repository.generate_otp(param=param)
        return GenerateOtpResponse(phoneNumber=param.phoneNumber,otp=result["otp"],message=result["message"])

    async def verify_otp(self, param:VerifyOtpParam):

        result=await self.repository.verify_otp(param=param)
        return result    
    
    async def create_profile(self, param:CreateProfileParam,userId:UUID):

        profile,user =await self.repository.create_profile(param=param,userId=userId)
        return OneProfileOut(user=user, profile=profile) 

    async def update_profile(self, param:UpdateProfileParam,userId=UUID) -> Profile:

        profile,user=await self.repository.update_profile(param=param,userId=userId)
        return OneProfileOut(profile=profile,user=user) 
    
        




