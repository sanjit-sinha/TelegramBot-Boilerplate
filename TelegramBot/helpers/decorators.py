"""
More about python decorators.
https://www.geeksforgeeks.org/decorators-in-python/
https://realpython.com/primer-on-python-decorators/
"""

from TelegramBot.helpers.functions import isAdmin
from pyrogram.types import Message
from TelegramBot.config import *
from functools import wraps
from pyrogram import Client
from typing import Callable


def sudo_commands(func: Callable) -> Callable:
    """
    Restricts user's from executing certain sudo user's' related commands
    """
    
    @wraps(func)
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERID:
            return await func(client, message)

    return decorator


def dev_commands(func: Callable) -> Callable:
    """
    Restricts user's from executing certain developer's related commands
    """
    
    @wraps(func)
    async def decorator(client: Client, message: Message):
        if message.from_user.id in OWNER_USERID:
            return await func(client, message)

    return decorator


def admin_commands(func: Callable) -> Callable:
    """
    Restricts user's from using group admin commands.
    """
    
    @wraps(func)
    async def decorator(client: Client, message: Message):
        if await isAdmin(message):
            return await func(client, message)

    return decorator


def errors(func: Callable) -> Callable:
    """
    Try and catch error of any function.
    """
    
    @wraps(func)
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as error:
            await message.reply(f"{type(error).__name__}: {error}")

    return decorator


from typing import Union

from cachetools import TTLCache
from pyrate_limiter import (
    BucketFullException,
    Duration,
    Limiter,
    MemoryListBucket,
    RequestRate)

class RateLimiter:
    """
    Impliments rate limit logic using leaky bucket
    algorithm, via pyrate_limiter.
    """

    def __init__(self) -> None:
     
        self.minute_rate = RequestRate(20, Duration.MINUTE)
        self.hourly_rate = RequestRate(1000, Duration.HOUR)
        self.daily_rate = RequestRate(10000, Duration.DAY)
       
        self.limiter = Limiter(
            self.minute_rate,
            self.hourly_rate,
            self.daily_rate,
            bucket_class=MemoryListBucket)

    def acquire(self, userid: Union[int, str]) -> bool:
        """
        Acquire rate limit per chat and return True / False
        based on chat's ratelimit status.
        """
        try:
            self.limiter.try_acquire(userid)
            return False
        except BucketFullException:
            return True


# initialize the ratelimiter
RATE_LIMITER = RateLimiter()
# store warned chats
WARNED_USERS = TTLCache(maxsize=128, ttl=60)
# message to send on spam
WARNING_MSG = "Spam detected! ignoring updates for sometime..."


def ratelimit(func: Callable) -> Callable:
    """
    Restricts user's from executing certain developer's related commands
    """
    
    @wraps(func)
    async def decorator(client: Client, message: Message):
        userid = message.from_user.id 
        is_limited = RATE_LIMITER.acquire(userid)
        
        if is_limited:
        	print("true")
        return await func(client, message)

    return decorator
