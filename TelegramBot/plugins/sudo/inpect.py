from pyrogram.types import Message 
from pyrogram import Client, filters
from pyrogram.errors import MessageTooLong

from TelegramBot.helpers.filters import sudo_cmd
from TelegramBot.helpers.decorators import ratelimiter
from TelegramBot.helpers.pasting_services import katbin_paste


@Client.on_message(filters.command("inspect") & sudo_cmd)
@ratelimiter
async def inspect(_, message: Message):
    """
    inspects the message and give reply in json format.
    """
    
    try:
        return await message.reply_text(message, quote=True)
    except MessageTooLong:
        output = await katbin_paste(message)
        return await message.reply_text(output, quote=True)
