from functools import wraps
from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from TelegramBot import loop
from TelegramBot.helpers.functions import isAdmin


def admin_commands(func: Callable) -> Callable:
    """Restricts user's from using group admin commands."""

    @wraps(func)
    async def decorator(client: Client, message: Message):
        if await isAdmin(message):
            return await func(client, message)

    return decorator


def catch_errors(func: Callable) -> Callable:
    """Try and catch error of any function."""

    @wraps(func)
    async def decorator(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except Exception as error:
            await message.reply(f"{type(error).__name__}: {error}")

    return decorator


# ====================================================================================
# SOME MORE USEFUL DECORATORS


def run_sync_in_thread(func: Callable) -> Callable:
    """
    A decorator for running a synchronous long running function asynchronously in a separate thread,
    without blocking the main event loop which make bot unresponsive.

    To use this decorator, apply it to any synchronous function, then you can then call that function to anywhere
    in your program and can use it along with await keyword. This will allow the function to be run asynchronously,
    and avoid blocking of the main event loop.
    see example at :- https://github.com/sanjit-sinha/TelegramBot-Boilerplate/blob/43ce589fbf7fbfcba6347d0e1945ac7299667e80/TelegramBot/plugins/sudo/speedtest.py#L13
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await loop.run_in_executor(None, func, *args, **kwargs)

    return wrapper
