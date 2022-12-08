from TelegramBot.helpers.decorators import dev_commands
from TelegramBot.logging import LOGGER
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *
import sys
import os

prefixes = COMMAND_PREFIXES


commands = ["update", f"update@{BOT_USERNAME}"]
@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def update(client, message: Message):
    """
    Update the bot with latest commit changes from GitHub.
    """

    msg = await message.reply_text(
        "**Pulling changes with latest commits...**", quote=True
    )
    os.system("git pull")
    LOGGER(__name__).info("Bot Updated with latest commits. Restarting now..")
    await msg.edit("**Changes pulled with latest commits. Restarting bot now... 🌟**")
    os.execl(sys.executable, sys.executable, "-m", "TelegramBot")
    sys.exit()


commands = ["restart", f"restart@{BOT_USERNAME}"]
@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def restart(client, message: Message):
    """
    This function just Restart the bot.
    """

    LOGGER(__name__).info("Restarting the bot. shutting down this instance")
    await message.reply_text("`Starting a new instance and shutting down this one`", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "TelegramBot")
    sys.exit()
