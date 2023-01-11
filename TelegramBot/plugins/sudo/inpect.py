from pyrogram import Client, filters
from pyrogram.errors import MessageTooLong

from TelegramBot.helpers.decorators import ratelimiter, sudo_commands
from TelegramBot.helpers.pasting_services import telegraph_paste


@Client.on_message(filters.command(["inspect"]))
@sudo_commands
@ratelimiter
async def inspect(_, message):
    """
    isnpect the message and give reply in json format.
    """
    try:
        await message.reply_text(message, quote=True)
    except MessageTooLong:
        output = await telegraph_paste(message)
        await message.reply_text(output, quote=True)
