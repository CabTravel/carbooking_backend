
import redis.asyncio as redis

from app.core.settings import get_settings

settings=get_settings()

redist_client=redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    decode_responses=True
)