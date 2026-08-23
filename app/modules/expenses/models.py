
from app.database.session import Base
from app.core.database.remote_db_table_base_mixin import RemoteDbTableMixin

from sqlalchemy import Column,String,Float,Numeric,BigInteger,UUID

class ExpenseModel(RemoteDbTableMixin, Base):

    __tablename__='expenses'
    localId=Column(String,unique=True,nullable=False)
    userId=Column(UUID,nullable=False)
    category=Column(String,nullable=False)
    amount=Column(Numeric,nullable=False,)
    date=Column(BigInteger,nullable=False)
    notes=Column(String)
    localCreateDate=Column(BigInteger)
    localUpdateDate=Column(BigInteger)








