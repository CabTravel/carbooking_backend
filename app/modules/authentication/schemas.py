from pydantic import BaseModel,Field,ConfigDict

from app.modules.authentication. models import User,Profile
from uuid import UUID
from pydantic import EmailStr


class OneFullUser(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    id: UUID
    email:str
    phoneNumber: str|None=None
    ownerName: str | None = None
    companyName: str | None = None
    logoImageUrl: str | None = None
    aboutCompany: str | None = None
    companyWebsite: str | None = None
    instagramProfile: str | None = None

    # @model_validator(mode="before")
    @classmethod
    def flatten_user(cls, value):

        # Already a dictionary / normal Pydantic input
        if isinstance(value, dict):
            return value

        # SQLAlchemy User object
        if hasattr(value, "profile"):

            profile = value.profile

            return {
                "id": value.id,
                "email": value.email,

                "phoneNumber":profile.phoneNumber if profile else None,
                "ownerName": profile.ownerName if profile else None,
                "companyName": profile.companyName if profile else None,
                "logoImageUrl": profile.logoImageUrl if profile else None,
                "aboutCompany": profile.aboutCompany if profile else None,
                "companyWebsite": profile.companyWebsite if profile else None,
                "instagramProfile": profile.instagramProfile if profile else None,
            }

        return value



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
    phoneNumber:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None

class UpdateProfileParam(BaseModel):
    ownerName:str
    phoneNumber:str
    companyName:str
    logoImageUrl:str|None
    aboutCompany:str|None
    companyWebsite:str
    instagramProfile:str|None


class OneProfileOut(BaseModel):
    user:OneFullUser


class LoginWithGoogleParam(BaseModel):
    email:EmailStr

class LoginWithGoogleOut(BaseModel):
    user:OneFullUser
    authToken:str
















