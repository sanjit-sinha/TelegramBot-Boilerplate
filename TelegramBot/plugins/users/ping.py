from time import time

from httpx import AsyncClient
from pyrogram import Client, filters

from TelegramBot import BotStartTime
from TelegramBot.config import prefixes
from TelegramBot.helpers.decorators import ratelimiter
from TelegramBot.helpers.functions import get_readable_time

commands = ["ping", "alive"]


@Client.on_message(filters.command(commands, **prefixes))
@ratelimiter
async def ping(_, message):
    """
    Give ping speed of Telegram API along with Bot Uptime.
    """
    pong_reply = await message.reply_text("pong!", quote=True)
    start = time()
    async with AsyncClient() as client:
        await client.get("http://api.telegram.org")
    end = time()
    botuptime = get_readable_time(time() - BotStartTime)
    pong = (end - start) / 1000
    return await pong_reply.edit(
        f"**Ping Time:** `{pong}`ms | **Bot is alive since:** `{botuptime}`"
    )
