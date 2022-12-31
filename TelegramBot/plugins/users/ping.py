from TelegramBot.helpers.functions import get_readable_time    
from TelegramBot.helpers.decorators import ratelimit
from pyrogram import Client, filters
from TelegramBot import BotStartTime
from pyrogram.types import Message
from TelegramBot.config import *
from datetime import datetime
import time
import httpx
import asyncio

	

commands = ["ping", "alive"]
@ratelimit
@Client.on_message(filters.command(commands, **prefixes))
async def ping(_, message: Message):
   """
   Give ping speed of Telegram API along with Bot Uptime.
   """
   
   pong_reply = await message.reply_text("pong!", quote=True)

   start = datetime.now()   
   async with httpx.AsyncClient() as client:
     	await client.get("http://api.telegram.org") 	
   end = datetime.now()
   
   botuptime = get_readable_time(time.time() - BotStartTime)
   pong = (end - start).microseconds / 1000
   
   return await pong_reply.edit(f"**Ping Time:** `{pong}`ms | **Bot is alive since:** `{botuptime}`")
   
   
