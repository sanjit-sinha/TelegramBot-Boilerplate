from TelegramBot.helpers.functions import get_readable_time    
from pyrogram import Client, filters
from TelegramBot import BotStartTime
from pyrogram.types import Message
from TelegramBot.config import *
from datetime import datetime
import time
import httpx

prefixes = COMMAND_PREFIXES
commands = ["ping", f"ping@{BOT_USERNAME}", "alive", f"alive@{BOT_USERNAME}"]

@Client.on_message(filters.command(commands, **prefixes))
async def ping(_, message: Message):
   """
   Give ping speed of Telegram API along with Bot Uptime.
   """

   start = datetime.now()
   
   async with httpx.AsyncClient() as client:
     	await client.get("http://api.telegram.org")
   	
   end = datetime.now()
   
   botuptime = get_readable_time(time.time() - BotStartTime)
   pong = (end - start).microseconds / 1000
   await message.reply_text(f"**Ping Time:** `{pong}`ms | **Bot is alive since:** `{botuptime}`", quote=True)
   
   
