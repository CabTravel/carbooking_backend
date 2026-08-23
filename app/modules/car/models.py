
from app.database.session import Base
from app.core.database.remote_db_table_base_mixin import RemoteDbTableMixin

from sqlalchemy import String,Column,Boolean,Integer,Numeric,BigInteger,ForeignKey,UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

class Car(RemoteDbTableMixin ,Base):
    __tablename__='cars'

    __table_args__ = (
        UniqueConstraint(
            "userId",
            "localId",
            name="uq_car_user_local_id",
        ),
    )
  
    localId=Column(String,nullable=False,unique=True)
    userId=Column(UUID,ForeignKey('users.id'),nullable=False,index=True)

    carNumber=Column(String,nullable=False)
    carBrandName=Column(String,nullable=False)
    isAc=Column(Boolean,default=True,nullable=False)
    tripType=Column(String,nullable=False)
    seats=Column(Integer,nullable=False)

    driverName=Column(String)
    driverphoneNumber=Column(String)
    withDriverPerKmPrice=Column(Numeric(12,3))
    withDriverPerDayPrice=Column(Numeric(12,3))
    withoutDriverPerKmPrice=Column(Numeric(12,3))
    withoutDriverPerDayPrice=Column(Numeric(12,3))

    localCreateDate=Column(BigInteger,nullable=False)
    localUpdateDate=Column(BigInteger,nullable=False)
    # Required
    coverImageUrl = Column(String(500),nullable=True)
    frontImageUrl = Column(String(500),nullable=True,)
    backImageUrl = Column(String(500),nullable=True,)
    leftImageUrl = Column(String(500),nullable=True,)
    rightImageUrl = Column(String(500),nullable=True,)










