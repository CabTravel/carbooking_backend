
from pydantic import BaseModel
class GenerateOtpParam(BaseModel):
    phoneNumber:str
    otp:str