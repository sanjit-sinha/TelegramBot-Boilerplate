from pyrogram.types import Message 
from pyrogram import Client, filters
from pyrogram.errors import MessageTooLong

from TelegramBot.helpers.decorators import ratelimiter
from TelegramBot.helpers.pasting_services import telegraph_paste


@Client.on_message(filters.command(["inspect"]) & SUDO_USERS)
@ratelimiter
async def inspect(_, message: Message):
    """
    isnpects the message and give reply in json format.
    """
    
    try:
        await message.reply_text(message, quote=True)
    except MessageTooLong:
        output = await telegraph_paste(message)
        await message.reply_text(output, quote=True)
