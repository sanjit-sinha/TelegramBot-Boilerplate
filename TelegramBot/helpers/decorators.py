"""
More about python decorators.
https://www.geeksforgeeks.org/decorators-in-python/
https://realpython.com/primer-on-python-decorators/
"""

from pyrogram.types import Message, CallbackQuery
from TelegramBot.helpers.functions import isAdmin
from TelegramBot.helpers.ratelimiter import RateLimiter 
from TelegramBot.config import *
from typing import Callable, Union
from cachetools import TTLCache
from functools import wraps
from pyrogram import Client


ratelimiter = RateLimiter()
warned_users = TTLCache(maxsize=128, ttl=600)
warning_message = "Spam detected! ignoring your all requests for few minutes."
    

def ratelimiter(func: Callable) -> Callable:
    """
    Restricts user's from spamming commands or pressing buttons multiple times
    using leaky bucket algorithm and pyrate_limiter.
    """
    
    @wraps(func)
    async def decorator(client: Client, update: Union[Message, CallbackQuery]):
	    userid = update.from_user.id
	    is_limited = ratelimiter.acquire(userid) ; print(warned_users)
	    
	    if is_limited and userid not in warned_users:
	    	if isinstance(update, Message):
	    		await update.reply_text(warning_message)
	    		warned_users[userid] = 1
	    		return
	    	
	    	elif isinstance(update, CallbackQuery):
	    		await update.answer(warning_message, show_alert=True)
	    		warned_users[userid] = 1
	    		return
	    
	    elif is_limited and userid in warned_users: pass
	    else: return await func(client, update)
   
    return decorator
    
    
def sudo_commands(func: Callable) -> Callable:
    """
    Restricts user's from executing certain sudo user's' related commands.
    """
    
    @wraps(func)
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERID:
            return await func(client, message)

    return decorator


def dev_commands(func: Callable) -> Callable:
    """
    Restricts user's from executing certain developer's related commands.
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


