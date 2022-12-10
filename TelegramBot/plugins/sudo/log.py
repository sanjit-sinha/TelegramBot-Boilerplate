from TelegramBot.helpers.decorators import sudo_commands
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *



commands = ["log", "logs"]
@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
async def log(client, message: Message):
    """
    upload log file of the bot.
    """
    
    try:
        await client.send_document(message.chat.id, "logs.txt", caption="logs.txt")
    except Exception as error:
        await message.reply_text(f"{error}", quote=True)
