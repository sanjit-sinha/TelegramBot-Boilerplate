from TelegramBot.config import BOT_TOKEN, API_ID, API_HASH
from TelegramBot.logging import LOGGER
from pyrogram import Client
import time
import sys

BotStartTime = time.time()
plugins = dict(root="TelegramBot/plugins")

if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    VERSION_ASCII ="""
  =============================================================
  You MUST need to be on python 3.7 or above, shutting down the bot...
  =============================================================
  """
    LOGGER(__name__).critical(VERSION_ASCII)
    sys.exit(1)


BANNER = """
____________________________________________________________________
|  _______   _                                ____        _        |
| |__   __| | |                              |  _ \      | |       |
|    | | ___| | ___  __ _ _ __ __ _ _ __ ___ | |_) | ___ | |_      |
|    | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \|  _ < / _ \| __|     |
|    | |  __/ |  __/ (_| | | | (_| | | | | | | |_) | (_) | |_      |
|    |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_|____/ \___/ \__|     |
|                    __/ |                                         |
|__________________________________________________________________|   
"""

# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

LOGGER(__name__).info(BANNER)
LOGGER(__name__).info("initiating the client...")

bot = Client(
    "TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins #https://docs.pyrogram.org/topics/smart-plugin
)
