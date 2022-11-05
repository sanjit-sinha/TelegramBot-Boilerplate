

from TelegramBot.helpers.decorators import dev_commands
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *


prefixes=COMMAND_PREFIXES  
commands=["log","logs", f"log@{BOT_USERNAME}", f"logs@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands,**prefixes))
@dev_commands
async def log(client, message: Message):
  """
  upload log file of the bot.
  """
  try : 
    await client.send_document(message.chat.id, "logs.txt", caption="logs.txt")
  except Exception as error: 
    await message.reply_text(f"{error}",  quote=True)
