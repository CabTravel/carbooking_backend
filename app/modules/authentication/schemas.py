from pydantic import BaseModel,Field,ConfigDict

from app.modules.authentication. models import User,Profile
from uuid import UUID

class UserOut(BaseModel):
    id:UUID
    phoneNumber:str
    model_config=ConfigDict(from_attributes=True)

        


class ProfileOut(BaseModel):
    id:UUID
    ownerName:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None

    model_config=ConfigDict(from_attributes=True)


class GenerateOtpRequest(BaseModel):
    phoneNumber:str=Field(min_length=10,max_length=10)

class GenerateOtpResponse(BaseModel):
    phoneNumber:str=Field(min_length=10,max_length=10)
    otp:str
    message:str|None

class VerifyOtpParam(BaseModel):
    phoneNumber:str=Field(min_length=10,max_length=10)
    otp:str=Field(min_length=4,max_length=4)





class VerifyOtpOut(BaseModel):
    user:UserOut
    profile:ProfileOut|None =None
    authToken:str



class CreateProfileParam(BaseModel):
    ownerName:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None

class UpdateProfileParam(BaseModel):
    id:str
    ownerName:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None


class OneProfileOut(BaseModel):
    user:UserOut
    profile:ProfileOut













