import os
from time import time
from shutil import disk_usage



from psutil import Process 
from psutil import cpu_percent
from psutil import virtual_memory
from psutil import disk_usage as disk_usage_percent

from pyrogram.types import Message 
from pyrogram import Client, filters

from TelegramBot import BotStartTime
from TelegramBot.helpers.filters import sudo_cmd
from TelegramBot.helpers.decorators import ratelimiter
from TelegramBot.helpers.functions import get_readable_bytes, get_readable_time


@Client.on_message(filters.command(["stats", "serverstats"]) & sudo_cmd)
@ratelimiter 
async def stats(_, message: Message):
    """
    Give system stats of the server.
    """

    currentTime = get_readable_time(time() - BotStartTime)
    total, used, free = disk_usage(".")
    total = get_readable_bytes(total)
    used = get_readable_bytes(used)
    free = get_readable_bytes(free)
    process = Process(os.getpid())
    
    caption = f"""
**≧◉◡◉≦ Bot is Up and Running successfully.**

Total Disk Space: `{total}`
Used: `{used}({disk_usage_percent("/").percent}%)`
Free: `{free}`

Cpu Usage: `{cpu_percent()}%`
Ram Usage: `{virtual_memory().percent}%`
Bot Uptime: `{currentTime}`
Bot Usage: `{round(process.memory_info()[0]/1024 ** 2)} MiB`
"""

    return await message.reply_animation(
        animation="https://telegra.ph/file/fd2495f0465f5293bd052.mp4",
        caption=caption,
        quote=True)
