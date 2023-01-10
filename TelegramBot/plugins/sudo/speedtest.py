from pyrogram import Client, filters
from pyrogram.types import Message
from speedtest import Speedtest

from TelegramBot import loop
from TelegramBot.config import prefixes
from TelegramBot.helpers.decorators import ratelimiter, sudo_commands
from TelegramBot.helpers.functions import get_readable_bytes
from TelegramBot.logging import LOGGER


def speedtestcli():
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    return test.results.dict()


commands = ["speedtest", "speed"]


@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
@ratelimiter
async def speedtest(_, message: Message):
    """
    Give speedtest of server where bot is running
    """
    speed = await message.reply("Running speedtest....", quote=True)
    LOGGER(__name__).info("Running speedtest....")
    result = await loop.run_in_executor(None, speedtestcli)

    speed_string = f"""
Upload: {get_readable_bytes(result["upload"] / 8)}/s
Download: {get_readable_bytes(result["download"] / 8)}/s
Ping: {result["ping"]} ms
ISP: {result["client"]["isp"]}
"""
    await speed.delete()
    return await message.reply_photo(
        photo=result["share"], caption=speed_string, quote=True
    )
