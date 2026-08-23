
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker

from app.core.settings import get_settings

Base=declarative_base()

settins=get_settings()


engine=create_async_engine(settins.database_url,future=True,echo=False)

async_session=async_sessionmaker(engine,expire_on_commit=False,class_=AsyncSession)

async def get_db():
    async with async_session as session:
        yield session




