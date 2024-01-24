#!/usr/bin/env python3
""" Writng strings to redis """

import redis
from typing import Union, Callable, Optional
import random
import uuid


class Cache():
    """ Redis class that stores an instance of the redis client """

    def __init__(self):
        """ Instance of the redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes data arg and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        Method that takes key and fn as callable
        convert the data back to the desired format
        """
        value = self._redis.get(key)

        if fn:
            value = fn(value)
            return value

    def get_str(self, key: str) -> str:
        """ Method that gets a string format of a value """
        value = self._redis.get(key, str)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Method that gets an int format of value """
        value = self._redis.get(key, int)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
            return value
