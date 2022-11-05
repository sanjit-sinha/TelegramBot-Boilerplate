from TelegramBot.helpers.functions import get_readable_time
from pyrogram import filters, Client 
from TelegramBot import BotStartTime 
from TelegramBot.config import * 
import time

prefixes=COMMAND_PREFIXES 
commands=["alive", f"alive@{BOT_USERNAME}"]

@Client.on_message(filters.command(commands,**prefixes))
async def alive(_, message):
    """
    To check if bot is alive or not with bot uptime message.
    """
    botuptime =  get_readable_time(time.time()-BotStartTime)
    await message.reply_text(f"**Bot is alive since {botuptime}.**", quote=True) 
