import asyncio
from functools import wraps
from cachetools import TTLCache
from typing import Callable, Union

from pyrogram import Client
from pyrogram.types import CallbackQuery, Message

from TelegramBot import loop
from TelegramBot.helpers.functions import isAdmin
from TelegramBot.helpers.ratelimiter import RateLimiter


ratelimit = RateLimiter()

# storing spammy user in cache for 1minute before allowing them to use commands again.
warned_users = TTLCache(maxsize=128, ttl=60)
warning_message = "Spam detected! ignoring your all requests for few minutes."


def ratelimiter(func: Callable) -> Callable:
    """
    Restricts user's from spamming commands or pressing buttons multiple times
    using leaky bucket algorithm and pyrate_limiter.
    """

    @wraps(func)
    async def decorator(client: Client, update: Union[Message, CallbackQuery]):
        userid = update.from_user.id
        is_limited = await ratelimit.acquire(userid)

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
    async def decorator(client, message, *args,**kwargs):
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
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await loop.run_in_executor(None, func, *args, **kwargs)
    
    return wrapper
