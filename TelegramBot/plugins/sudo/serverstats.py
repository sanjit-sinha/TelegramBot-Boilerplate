from shutil import disk_usage
from time import time

from psutil import cpu_percent
from psutil import disk_usage as disk_usage_percent
from psutil import virtual_memory
from pyrogram import Client, filters

from TelegramBot import BotStartTime
from TelegramBot.config import prefixes
from TelegramBot.helpers.decorators import ratelimiter, sudo_commands
from TelegramBot.helpers.functions import get_readable_bytes, get_readable_time

commands = ["stats", "serverstats"]


@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
@ratelimiter
async def stats(_, message):

    currentTime = get_readable_time(time() - BotStartTime)
    total, used, free = disk_usage(".")
    total = get_readable_bytes(total)
    used = get_readable_bytes(used)
    free = get_readable_bytes(free)
    caption = f"""
f"**≧◉◡◉≦ Bot is Up and Running successfully.**

Bot Uptime: `{currentTime}`
Total Disk Space: `{total}`
Used: `{used}({disk_usage_percent("/").percent}%)`
Free: `{free}`
CPU Usage: `{cpu_percent()}%`
RAM Usage: `{virtual_memory().percent}%`"
"""
    return await message.reply_animation(
        animation="https://telegra.ph/file/fd2495f0465f5293bd052.mp4",
        caption=caption,
        quote=True,
    )
