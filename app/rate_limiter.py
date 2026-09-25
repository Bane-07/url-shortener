import os
import redis

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379"
)

redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True
)

def is_rate_limited(identifier: str, limit: int = 12, window: int = 60):
    key = f"rate_limit:{identifier}"

    count = redis_client.incr(key)

    if count == 1:
        redis_client.expire(key, window)

    return count > limit

