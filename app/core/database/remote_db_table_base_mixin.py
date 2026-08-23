from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime,BigInteger,Integer,text
from sqlalchemy.dialects.postgresql import UUID

from app.database.session import Base

def current_time_millis() -> int:
    return int(
        datetime.now(timezone.utc).timestamp() * 1000
    )

class RemoteDbTableMixin:
    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=text("gen_random_uuid()")
    )

    create_date = Column(
        BigInteger,
        default=current_time_millis,
        nullable=False,
    )

    update_date = Column(
        BigInteger,
        default=current_time_millis,
        onupdate=current_time_millis,
        nullable=False,
    )


