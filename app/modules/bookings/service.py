
from app.modules.bookings.repository import BookingRepository
from uuid import UUID
from app.core.server_response import SuccessResponse

from app.modules.bookings.schemas import OneBookingOut,BookingsListOut,CreateBookingParam,UpdateBookingParam,PatchBookingParam
from fastapi import Depends
class BookingService:

    def __int__(self,repository:BookingRepository=Depends()):
        self.repository=repository


    async def get_bookings_by_userId(self,userId:UUID):

        result=await self.repository.get_booking_userid(userId=userId)

        return BookingsListOut(bookings=result)

       

    async def get_booking_by_id(self, booking_id:UUID):
        result= await self.repository.get_booking_by_id(id=booking_id)

        return OneBookingOut(booking=result)

        

    async def create_booking(self,param:CreateBookingParam,userId:UUID):

        result= await self.repository.create_booking(userId=userId,param=param)

        return OneBookingOut(booking=result)

       

    async def update_booking(self,param:UpdateBookingParam):
        result=await self.repository.update_booking(param=param)

        return OneBookingOut(booking=result)

    

    async def patch_booking(self,param:PatchBookingParam):

        result=await self.repository.patch_booking(param=param)

        return OneBookingOut(booking=result)

       

    async def delete_booking(self,booking_id:UUID):

        result=await self.repository.delete(id=booking_id)

        return OneBookingOut(booking=result)

    

    
    



    
        