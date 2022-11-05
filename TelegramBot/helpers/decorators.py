"""
About python decorators.
https://www.geeksforgeeks.org/decorators-in-python/
https://realpython.com/primer-on-python-decorators/
"""

from TelegramBot.helpers.functions import isAdmin
from pyrogram import Client 
from typing import Callable
from TelegramBot.config import * 
from pyrogram.types import Message


def sudo_commands(func: Callable) -> Callable:
	"""
	Restricts user's from executing certain sudo user's' related commands
	"""
	async def decorator(client: Client, message: Message):
	    if message.from_user.id in SUDO_USERID:
	        return await func(client, message)
	return decorator



def dev_commands(func: Callable) -> Callable:
	"""
	Restricts user's from executing certain developer's related commands
	"""
	async def decorator(client: Client, message: Message):
	     if message.from_user.id in OWNER_USERID:
	     	return await func(client, message)
	return decorator
 
def admin_commands(func: Callable) -> Callable:
    """
    Restricts user's from using group admin commands.
    """
    async def decorator(client: Client, message: Message):
    	if await isAdmin(message):
    		return await func(client, message)
    return decorator



def errors(func: Callable) -> Callable:
    """
    Try and catch error of any function.
    """
    async def decorator(client: Client, message: Message):
        try:
        	return await func(client, message)
        except Exception as error:
        	await message.reply(f"{type(error).__name__}: {error}")
    return decorator
