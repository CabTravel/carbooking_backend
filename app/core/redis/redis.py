
import redis.asyncio as redis

from app.core.settings import get_settings

settings=get_settings()

redist_client=redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)