from TelegramBot.helpers.functions import get_readable_bytes
from TelegramBot.helpers.decorators import sudo_commands
from TelegramBot.logging import LOGGER
from speedtest import Speedtest 
from pyrogram.types import Message
from pyrogram import Client, filters
from TelegramBot.config import *

prefixes=COMMAND_PREFIXES 
commands=["speedtest", f"speedtest@{BOT_USERNAME}"]

@Client.on_message(filters.command(commands,**prefixes))
@sudo_commands
async def speedtest(_, message: Message):
    """
    Give speedtest of server where bot is running
    """
    speed = await message.reply("**Running speedtest ....**" , quote=True)
    LOGGER(__name__).info("speedtest starter")
    
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    photo = (result['share'])
    
    string_speed = f'''
× Upload: {get_readable_bytes(result["upload"] / 8)}/s
× Download: {get_readable_bytes(result["download"] / 8)}/s
× Ping: {result["ping"]} ms
× ISP: {result["client"]["isp"]}
'''
    await speed.delete()
    await message.reply_photo(photo=photo, caption=string_speed, quote=True)

        
