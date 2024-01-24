#!/usr/bin/env python3
"""
Implement a get_page function that uses requests module to
obtain HTML content of a particular URL and returns it
"""

import redis
from typing import Callable
from functools import wraps
import requests


def count_url(method: Callable) -> Callable:
    """ Tracks and counts number of times a URL was accessed in a key"""

    @wraps(method)
    def wrapper(*args, **kwds):
        """ The r=function to be returned"""
        cache = redis.Redis()
        key = f"count:{args[0]}"
        cache.incrby(key, 1)
        cache.expire(key, 10)
        return method(*args, **kwds).text
    return wrapper


@count_url
def get_page(url: str) -> str:
    """ Uses requests to obtain the HTML content of a particular url"""
    results = requests.get(url)
    return results
