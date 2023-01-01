from TelegramBot.helpers.decorators import sudo_commands, ratelimiter
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *


commands = ["log", "logs"]
@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
@ratelimiter
async def log(client: Client, message: Message):
    """
    upload log file of the bot.
    """
    
    try:
        await client.send_document(message.chat.id, "logs.txt", caption="logs.txt")
    except Exception as error:
        await message.reply_text(f"{error}", quote=True)
