
from app.modules.authentication. repository import AuthRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.authentication.schemas import GenerateOtpRequest,VerifyOtpParam,CreateProfileParam,UpdateProfileParam,LoginWithGoogleParam,LoginWithGoogleOut,OneFullUser
from uuid import UUID
from app.modules.authentication.schemas import Profile,GenerateOtpResponse,OneProfileOut

from fastapi import Depends

class AuthService:
    def __init__(self,repository:AuthRepository=Depends()):
        self.repository=repository



    async def login_with_google(self,param:LoginWithGoogleParam):

        result = await self.repository.login_with_google(param=param)
        user= OneFullUser.model_config(result[0])
        authToken=result[1]
        return LoginWithGoogleOut(user=user,authToken=authToken)


    async def generate_otp(self, param:GenerateOtpRequest):

        result=await self.repository.generate_otp(param=param)
        return GenerateOtpResponse(phoneNumber=param.phoneNumber,otp=result["otp"],message=result["message"])

    async def verify_otp(self, param:VerifyOtpParam):

        result=await self.repository.verify_otp(param=param)
        return result    
    
    async def create_profile(self, param:CreateProfileParam,userId:UUID):

        user =await self.repository.create_profile(param=param,userId=userId)

        return OneProfileOut(user=OneFullUser.model_config(user)) 

    async def update_profile(self, param:UpdateProfileParam,userId=UUID) -> Profile:

        user=await self.repository.update_profile(param=param,userId=userId)

        user= OneFullUser.model_config(user)
        return OneProfileOut(user=user) 
    
        




