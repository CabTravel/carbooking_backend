
from app.database.session import Base
from app.core.database.remote_db_table_base_mixin import RemoteDbTableMixin
from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
class User(RemoteDbTableMixin, Base):
    __tablename__='users'

    phoneNumber=Column(

        String(10),
        nullable=False,
        unique=True,
        index=True
    )

    profile=relationship(
        'Profile',
        back_populates='user',
        uselist=False
    )

class Profile(RemoteDbTableMixin,Base):
    __tablename__='profiles'
    userId=Column(UUID(as_uuid=True),ForeignKey('users.id'),nullable=False,unique=True,index=True)
    ownerName=Column(String(100))
    companyName=Column(String(150))
    logoImageUrl=Column(String)
    aboutCompany=Column(String(10000))
    companyWebsite=Column(String(500))
    instagramProfile=Column(String(500))

    user=relationship(
        "User",
        back_populates='profile',
    )









    


    