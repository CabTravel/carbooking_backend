
from app.modules.bookings.repository import BookingRepository
from uuid import UUID
from app.core.server_response import SuccessResponse

from app.modules.bookings.schemas import OneBookingOut,BookingsListOut,CreateBookingParam,UpdateBookingParam,PatchBookingParam,CreateMultipleBookingsParam,UpdateMultipleBookingsParam,CreateMultipleBookingsOut,UpdateMultipleBookingsOut
from fastapi import Depends
class BookingService:


    def __init__ (self,repository:BookingRepository=Depends()):
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

    async def create_multiple_bookings(self,param:CreateMultipleBookingsParam,userId:UUID):

        result= await self.repository.create_multiple(userId=userId,param=param)
        result= CreateMultipleBookingsOut(
            createdBookings=result[0],
            failedBookings=result[1],
            reasons=result[2]
        )
        return result

       

    async def update_booking(self,param:UpdateBookingParam):
        result=await self.repository.update_booking(param=param)

        return OneBookingOut(booking=result)


    async def update_multiple_bookings(self,userId:UUID, param:UpdateMultipleBookingsParam):

        result=await self.repository.update_multiple(userId=userId,param=param)
        result= UpdateMultipleBookingsOut(
            updatedBookings=result[0],
            failedBookings=result[1],
            reasons=result[2]
        )
        return result


    async def patch_booking(self,param:PatchBookingParam):

        result=await self.repository.patch_booking(param=param)

        return OneBookingOut(booking=result)

       

    async def delete_booking(self,booking_id:UUID):

        result=await self.repository.delete(id=booking_id)

        return OneBookingOut(booking=result)

    

    
    



    
        