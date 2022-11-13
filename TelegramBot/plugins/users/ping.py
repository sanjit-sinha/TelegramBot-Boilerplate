from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *
from datetime import datetime
import requests as r

prefixes = COMMAND_PREFIXES
commands = ["ping", f"ping@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
async def ping(_, message: Message):
   """
   Checks ping speed of Telegram API.
   """

   start = datetime.now()
   r.get("http://api.telegram.org")
   end = datetime.now()

   pong = (end - start).microseconds / 1000
   await message.reply_text(f"**PONG!!** | Ping Time: `{pong}`ms", quote=True)
