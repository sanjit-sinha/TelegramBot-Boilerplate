from TelegramBot.helpers.pasting_services import telegraph_paste
from TelegramBot.helpers.decorators import sudo_commands, ratelimiter
from pyrogram.errors import MessageTooLong
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *


commands = ["inspect"]	
@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
@ratelimiter
async def inspect(client: Client, message: Message):
  """
  isnpect the message and give reply in json format.
  """

  try:
      await message.reply_text(message, quote=True)
  except MessageTooLong:
      output = await telegraph_paste(message)
      await message.reply_text(output, quote=True)
	   
	
