from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.security import create_access_token
from app.modules.authentication.helping_methods import generate_otp
from fastapi import status,HTTPException
from uuid import UUID

from app.core.exceptions.exceptions import AppException

from app.core.services.redis.redis import redist_client
from  app.modules.authentication.schemas import VerifyOtpParam,VerifyOtpOut,CreateProfileParam,UpdateProfileParam,GenerateOtpRequest,UserOut
from app.modules.authentication.models import User,Profile

from fastapi import Depends
from app.database.session import get_db



class AuthRepository:
    def __init__(self,db:AsyncSession=Depends(get_db)):
        self.db=db



    async def get_user_by_phone_or_none(self,phoneNumber:str)-> User|None:

        result=await self.db.execute(select(User).where(User.phoneNumber==phoneNumber))

        user= result.scalar_one_or_none()
        return user
    


    async def generate_otp(self,param:GenerateOtpRequest):

        try:
            my_otp=generate_otp()
            key=f"otp:{param.phoneNumber}"

            await redist_client.set(
                key, my_otp, ex=300 )
            value=await redist_client.get(key)


            return {
                "otp":my_otp,
                "message":f"Saved otp is {value}"
                    }
            
        except Exception as e:
            raise AppException(status_code=500, message='Failed to generate otp')

    async def verify_otp(self,param:VerifyOtpParam):

        try:      
            key=f"otp:{param.phoneNumber}"
            value=await redist_client.get(key)
            if(value==None):
                raise AppException(
                    message='Otp Expired',
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            if value==param.otp:
                user=await self.get_user_by_phone_or_none(phoneNumber=param.phoneNumber)

                if user is None:
                    user=await self.create_user(phoneNumber=param.phoneNumber)
                    profile=None
                else:
                    profile=await self.get_profile_by_user_id(user.id)

                authToken= create_access_token(user_id=user.id)


                await redist_client.delete(key)
                return VerifyOtpOut(
                    user= user,
                    profile=profile,
                    authToken=authToken
                
                )

            else:
                raise AppException(
                    message='Invalid Otp ',
                    status_code=status.HTTP_400_BAD_REQUEST
                ) 
                
        except Exception as e:
            raise AppException(status_code=500, message=f'Failed to verify otp {str(e)}')



    async def get_user_by_phone(self,phoneNumber:str)-> User|None:

        result=await self.db.execute(select(User).where(User.phoneNumber==phoneNumber))

        user= result.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No user exist with phonenumber')
    

    async def get_profile_by_user_id(self,userId)-> Profile|None:

        result= await self.db.execute(select(Profile).where(Profile.userId==userId))
        return result.scalar_one_or_none()

    async def get_profile_by_id(self,id:UUID)-> Profile|None:

        result= await self.db.execute(select(Profile).where(Profile.id==id))
        return result.scalar_one_or_none()

    async def create_user(self,phoneNumber:str):
        user=User(phoneNumber=phoneNumber)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def create_profile(self,param:CreateProfileParam,userId:UUID)-> Profile:
        try:

            preProfile=await self.get_profile_by_user_id(userId=userId)

            if preProfile !=None:
                return preProfile
            

            profile=Profile(
            userId=userId,
            ownerName=param.ownerName,
            companyName=param.companyName,
        
            logoImageUrl=param.logoImageUrl,
            aboutCompany=param.aboutCompany,
            companyWebsite=param.companyWebsite )

            self.db.add(profile)
            await self.db.commit()
            await self.db.refresh(profile)

            return profile
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail= f"Internal Server error {str(e)}"
                                )


    async def update_profile(self,param:UpdateProfileParam,userId:UUID)-> Profile:
   
        profile=await self.get_profile_by_id(id=UUID(param.id))

        if profile is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Profile exists with id")
        
        profile.ownerName=param.ownerName
        profile.logoImageUrl=param.logoImageUrl
        profile.companyName=param.companyName
        profile.aboutCompany=param.aboutCompany
        profile.companyWebsite=param.companyWebsite
         
        
        await self.db.commit()
        await self.db.refresh(profile)

        return profile
    







        




        

