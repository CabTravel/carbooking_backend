
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.modules.bookings. models import Booking
from sqlalchemy import select
from fastapi import HTTPException,status,Depends
from app.database.session import get_db
from app.modules.bookings.schemas import CreateBookingParam,UpdateBookingParam,PatchBookingParam

class BookingRepository:

    def __int__(self,db:AsyncSession=Depends(get_db)):
        self.db=db


    async def get_booking_by_id(self,id:UUID)-> Booking:
        result= await self.db.execute(select(Booking).where(Booking.id==id))

        booking=result.scalar_one_or_none()

        if booking is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="NO Booking Exist with id")

        return booking


    async def get_booking_userid(self,userId:UUID):

        result= await self.db.execute(select(Booking).where(Booking.userId==userId))

        myList=result.scalars().all()

        return myList

    async def create_booking(self,userId:UUID, param:CreateBookingParam):

        booking=Booking(
            localId=param.localId,
            userId=userId,
            carName=param.carName,
            carNumber=param.carNumber,
            customerName=param.customerName,
            customerPhoneNumber=param.customerPhoneNumber,
            amout=param.amout,
            bookingDate=param.bookingDate,
            fromStation=param.fromStation,
            tostation=param.toStation,
            notes=param.notes,
            carLocalId=param.carLocalId,
            localCreateDate=param.localCreateDate,
            localUpdateDate=param.localUpdateDate

        )

        self.db.add(booking)
        await self.db.commit()
        await self.db.refresh(booking)

        return booking

  


    async def update_booking(self,param:UpdateBookingParam):

        booking=await self.get_booking_by_id(id=UUID(param.id))

        if booking is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found with id")

        booking.carName=param.carName
        booking.carNumber=param.carNumber
        booking.customerName=param.customerName
        booking.customerPhoneNumber=param.customerPhoneNumber
        booking.amount=param.amout
        booking.bookingDate=param.bookingDate
        booking.fromStation=param.fromStation
        booking.toStation=param.toStation
        booking.notes=param.notes
        booking.carLocalId=param.carLocalId
        booking.localUpdateDate=param.localUpdateDate


        await self.db.commit()
        await self.db.refresh(booking)

        return booking
     

    async def patch_booking(self,param:PatchBookingParam):

        booking=await self.get_booking_by_id(id=UUID(param.id))

        if booking is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found with id")

        data=param.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(booking, field, value)

        await self.db.commit()
        await self.db.refresh(booking)

        return booking
    

    async def delete(self,id:UUID):

        booking=await self.get_booking_by_id(id=id)
        if booking is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found with id")

        await self.db.delete(booking)
        await self.db.commit()
        return booking



        

        





        




        






    






    


    
        
