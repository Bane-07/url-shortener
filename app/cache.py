import os
import redis
from datetime import datetime

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379"
)

redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True
)


def get_cached_url(short_code: str):
    try:
        return redis_client.get(short_code)
    except redis.RedisError:
        return None


def cached_url(
    short_code: str,
    original_url: str,
    expires_at=None,
    ttl: int = 86400
):
    try:
        if expires_at:
            ttl = max(1, int((expires_at - datetime.utcnow()).total_seconds()))

        redis_client.set(
            short_code,
            original_url,
            ex=ttl
        )
    except redis.RedisError:
        pass