from pydantic import BaseModel,Field

from app.modules.authentication. models import User,Profile


class UserOut(BaseModel):
    id:str
    phoneNumber:str

class ProfileOut(BaseModel):
    id:str
    ownerName:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None


    


class GenerateOtpRequest(BaseModel):
    phoneNumber:str=Field(min_length=10,max_length=10)

class GenerateOtpResponse(BaseModel):
    phoneNumber:str=Field(min_length=10,max_length=10)

class VerifyOtpParam(BaseModel):
    phoneNumber:str=Field(min_length=10,max_length=10)
    otp:str=Field(min_length=4,max_length=4)




class VerifyOtpOut(BaseModel):
    user:UserOut
    profile:ProfileOut|None =None


class CreateProfileParam(BaseModel):
    ownerName:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None

class UpdateProfileParam(BaseModel):
    ownerName:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None













