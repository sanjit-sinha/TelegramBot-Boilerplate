from TelegramBot.helpers.functions import get_readable_time
from pyrogram import filters, Client
from TelegramBot import BotStartTime
from TelegramBot.config import *
from datetime import datetime
import requests as r
import time

prefixes = COMMAND_PREFIXES
commands = ["alive", f"alive@{BOT_USERNAME}", "ping", f"ping@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
async def alive(_, message):
    """
    To check if bot is alive or not with bot uptime message and ping speed of telegram API.
    """
    
    botuptime = get_readable_time(time.time() - BotStartTime)
    
    start = datetime.now()
    r.get("http://api.telegram.org")
    end = datetime.now()
    pong = (end - start).microseconds / 1000
    
    await message.reply_text(f"**Bot is alive since {botuptime}. ping Time: `{pong}`ms**", quote=True)   
