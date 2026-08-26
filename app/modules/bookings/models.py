from app.database.session import Base
from sqlalchemy import UniqueConstraint, Column,String,Float,Integer,ForeignKey,BigInteger
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.remote_db_table_base_mixin import RemoteDbTableMixin

class Booking(RemoteDbTableMixin,Base):
    __tablename__='bookings'

    __table_args__ = (
        UniqueConstraint(
            "userId",
            "localId",
            name="uq_booking_user_local_id",
        ),
    )
    userId=Column(UUID(as_uuid=True),ForeignKey("users.id"),index=True ,nullable=False,)
    localId=Column(String,nullable=False)
    carName=Column(String(length=100),nullable=False)
    carNumber=Column(String(length=100),nullable=False)
    customerName=Column(String(length=500),nullable=False)
    customerPhoneNumber=Column(String(length=10),nullable=False)
    amount=Column(Float,nullable=False)
    bookingDate=Column(BigInteger,nullable=False)
    fromStation=Column(String,nullable=False)
    toStation=Column(String,nullable=False)
    notes=Column(String,nullable=True)
    carLocalId=Column(String,)
    localCreateDate=Column(BigInteger,nullable=False)
    localUpdateDate=Column(BigInteger,nullable=False)




    



