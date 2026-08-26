from fastapi import APIRouter,Depends

from uuid import UUID
from app.core.security import get_current_user_id
from app.core.server_response import SuccessResponse
from app.modules.bookings.service import BookingService
from app.modules.bookings.schemas import CreateBookingParam,UpdateBookingParam,PatchBookingParam

from app.core.server_response import SuccessResponse


router=APIRouter(prefix='/bookings')

@router.get('',response_model=SuccessResponse)
async def get_booking_by_id(service:BookingService=Depends(), userId:UUID=Depends(get_current_user_id)):

    result= await service.get_bookings_by_userId(userId=userId)
    return SuccessResponse(data=result)

@router.get('/{id}',response_model=SuccessResponse)
async def get_booking_by_id(id:str, service:BookingService=Depends(), userId:UUID=Depends(get_current_user_id)):

    result= await service.get_booking_by_id(booking_id=UUID(id))
    return SuccessResponse(data=result)


@router.post('',response_model=SuccessResponse)
async def create_booking(param:CreateBookingParam, service:BookingService=Depends(), userId:UUID=Depends(get_current_user_id)):
    
    result= await service.create_booking(param=param,userId=userId)
    return SuccessResponse(data=result)

@router.put('',response_model=SuccessResponse)
async def update_booking(param:UpdateBookingParam ,service:BookingService=Depends(), userId:UUID=Depends(get_current_user_id)):

    result= await service.update_booking(param=param)
    return SuccessResponse(data=result)

@router.patch('',response_model=SuccessResponse)
async def patch_booking(param:PatchBookingParam ,service:BookingService=Depends(), userId:UUID=Depends(get_current_user_id)):

    result= await service.patch_booking(param=param)
    return SuccessResponse(data=result)

@router.delete('/{id}',response_model=SuccessResponse)
async def delete_booking(id:str ,service:BookingService=Depends(), userId:UUID=Depends(get_current_user_id)):
    result= await service.delete_booking(booking_id=UUID(id))
    return SuccessResponse(data=result)