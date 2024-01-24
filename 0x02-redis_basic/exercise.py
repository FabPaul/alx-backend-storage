#!/usr/bin/env python3
""" Writng strings to redis """

import redis
from typing import Union
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
    
    def get(self, key, fn):
        """ Method that takes key and fn as callable """
        value = self._redis.get(key)

        if fn:
            value = fn(value)
            return value
        
    def get_str(self, key):
        """ Method that gets a string format of a value """
        string = self.get(key, str)
        return string
    
    def get_int(self, key):
        """ Method that gets an int format of value """
        integer = self.get(key, int)
        return integer
