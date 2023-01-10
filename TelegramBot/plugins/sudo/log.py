from pyrogram import Client, filters

from TelegramBot.config import prefixes
from TelegramBot.helpers.decorators import ratelimiter, sudo_commands

commands = ["log", "logs"]


@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
@ratelimiter
async def log(_, message):
    """
    upload log file of the bot.
    """

    try:
        await message.reply_document("logs.txt", caption="logs.txt", quote=True)
    except Exception as error:
        await message.reply_text(f"{error}", quote=True)
