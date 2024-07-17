#!/usr/bin/env python3
"""Cache class."""
import redis
import uuid
from typing import Union


class Cache():
    """Redis client."""

    def __init__(self):
        """Store an instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Take data and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None)\
            -> Union[str, bytes, int, float, None]:
        """Read from redis and recover original type."""
        data = self._redis.get("key")
        if data is not None and fn is not None and callable(fn):
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get dataas string from redis."""
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data

    def get_int(self, key: str) -> int:
        """Get data as int."""
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data
