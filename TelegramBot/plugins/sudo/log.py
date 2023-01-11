from pyrogram.types import Message 
from pyrogram import Client, filters

from TelegramBot.helpers.decorators import ratelimiter


@Client.on_message(filters.command(["log", "logs"]) & SUDO_COMMAND)
@ratelimiter
async def log(_, message: Message):
    """
    upload the log file of the bot.
    """

    try:
        await message.reply_document("logs.txt", caption="logs.txt", quote=True)
    except Exception as error:
        await message.reply_text(f"{error}", quote=True)
