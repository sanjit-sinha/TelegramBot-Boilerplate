import shutil
import psutil
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot import BotStartTime
from TelegramBot.config import *
from TelegramBot.helpers.functions import get_readable_bytes, get_readable_time
from TelegramBot.helpers.decorators import sudo_commands


commands = ["stats", "serverstats"]
@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
async def stats(client: Client, message: Message):

    currentTime = get_readable_time(time.time() - BotStartTime)
    total, used, free = shutil.disk_usage(".")
    total = get_readable_bytes(total)
    used = get_readable_bytes(used)
    free = get_readable_bytes(free)

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    await message.reply_animation(
        animation="https://telegra.ph/file/fd2495f0465f5293bd052.mp4",
        caption=f"**≧◉◡◉≦ Bot is Up and Running successfully.**\n\n× Bot Uptime: `{currentTime}`\n× Total Disk Space: `{total}`\n× Used: `{used}({disk_usage}%)`\n× Free: `{free}`\n× CPU Usage: `{cpu_usage}%`\n× RAM Usage: `{ram_usage}%`",
        quote=True)
