from pyrogram.types import Message 
from pyrogram import Client, filters

from TelegramBot.helpers.filters import sudo_cmd
from TelegramBot.helpers.decorators import ratelimiter


@Client.on_message(filters.command(["log", "logs"]) & sudo_cmd)
@ratelimiter
async def log(_, message: Message):
    """
    upload the logs file of the bot.
    """

    try:
        return await message.reply_document("logs.txt", caption="logs.txt", quote=True)
    except Exception as error:
        return await message.reply_text(f"{error}", quote=True)
