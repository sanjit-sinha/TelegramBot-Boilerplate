from httpx import AsyncClient
from pyrogram import Client, filters
from pyrogram.types import Message

from TelegramBot.config import prefixes
from TelegramBot.helpers.decorators import dev_commands, ratelimiter

commands = ["ip"]


@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
@ratelimiter
async def ipinfo(_, message: Message):
    """
    Give ip of the server where bot is running.
    """
    async with AsyncClient() as client:
        response = await client.get("http://ipinfo.io/ip")
    await message.reply_text(f"IP Adress of server is: `{response.text}`", quote=True)
