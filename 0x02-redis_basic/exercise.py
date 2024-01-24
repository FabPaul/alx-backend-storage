#!/usr/bin/env python3
""" Writng strings to redis """

import redis
from typing import Union, Callable, Optional
import random
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator that takes a callable arg and returns callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Decorator to conserve the original function's name """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the historyof inputs and outputs for a func"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper to retriebe output """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwds))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(method: Callable):
    """ Displays the history of calls of a particular function"""
    cache = redis.Redis()
    input = method.__qualname__ + ":inputs"
    output = method.__qualname__ + ":outputs"
    call_freq = cache.llen(input)
    in_list = cache.lrange(input, 0, -1)
    out_list = cache.lrange(output, 0, -1)

    print(f"Cache.store was called {call_freq} times")
    for i in range(len(in_list)):
        print(f"{method.__qualname__}(*({in_list[i].decode('utf-8')}.)) -> {out_list.decode('utf-8')}")


class Cache():
    """ Redis class that stores an instance of the redis client """

    def __init__(self):
        """ Instance of the redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes data arg and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
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
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Method that gets an int format of value """
        value = self._redis.get(key)

        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
