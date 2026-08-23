

from fastapi import APIRouter,Depends,HTTPException,Depends
from app.modules.authentication.schemas import GenerateOtpRequest,VerifyOtpParam,CreateProfileParam,UpdateProfileParam

from app.core.server_response import SuccessResponse,failureFromException,FailureResponse
from uuid import UUID
from app.modules.authentication.service import AuthService

from app.core.security import get_current_user_id


router=APIRouter(prefix='/auth')

@router.post('/generateOtp',response_model=SuccessResponse)
async def generateOtp(request:GenerateOtpRequest,service:AuthService=Depends()):
    result= await service.generate_otp(param=request )
    return SuccessResponse(message='Otp generated successfully check message')

@router.post('/verifyOtp')
async def verifyOtp(param:VerifyOtpParam,service:AuthService=Depends()):
    result= await service.verify_otp(param=param)
    return SuccessResponse(
        data=result
    )

@router.post('/createProfile',response_model=SuccessResponse)
async def createProfile(param:CreateProfileParam,service:AuthService=Depends(),userId:UUID=Depends(get_current_user_id)):

    result= await service.create_profile(param=param)
    return SuccessResponse(
        data=result )

@router.put('/updateProfile',response_model=SuccessResponse)
async def updateProfile(param:UpdateProfileParam,service:AuthService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.update_profile(param=param,userId=userId)

    return SuccessResponse(
        data=result
    )





    

    







    
       
  
    
        
   
