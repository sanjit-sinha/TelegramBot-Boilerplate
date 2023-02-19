import os
import time 
import datetime
from shutil import disk_usage
from PIL import Image, ImageDraw, ImageFont

from psutil import Process 
from psutil import cpu_percent
from psutil import virtual_memory
from psutil import disk_usage as disk_usage_percent

from pyrogram import Client, filters
from pyrogram.types import Message 
from pyrogram.types import Message, InputMediaPhoto


from TelegramBot import BotStartTime
from TelegramBot.helpers.filters import sudo_cmd
from TelegramBot.helpers.decorators import ratelimiter
from TelegramBot.helpers.functions import get_readable_bytes, get_readable_time


@Client.on_message(filters.command(["stats", "serverstats"]) & sudo_cmd)
@ratelimiter 
async def stats(_, message: Message):
    botuptime = get_readable_time(time.time() - BotStartTime)
    start = datetime.now()
    msg = await message.reply_photo(photo="https://te.legra.ph/file/30a82c22854971d0232c7.jpg", quote=True)
    end = datetime.now()
	
	
    image = Image.open('TelegramBot/assets/StatsBg.png').convert('RGB')
    IronFont = ImageFont.truetype("TelegramBot/assets/IronFont.otf", 38)
    draw = ImageDraw.Draw(image)
    
    def draw_progressbar(coordinate, progress):
    	progress = 110+ (progress*10.8)
    	draw.ellipse((105, coordinate-25, 127 , coordinate), fill='#FFFFFF')
    	draw.rectangle((120, coordinate, progress, coordinate-25), fill='#FFFFFF')	
    	draw.ellipse((progress-7, coordinate-25, progress+15, coordinate), fill='#FFFFFF') 
    
    uptime = get_readable_time(time.time() - BotStartTime)
    total, used, free = shutil.disk_usage(".")
	
    cpu_percentage = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    draw_progressbar(243, int(cpu_percentage))
    draw.text((225,153), f"( {cpu_count} core, {cpu_percentage}% )", (255, 255, 255), font=IronFont)
	
    disk_percenatge = psutil.disk_usage("/").percent
    disk_total = get_readable_size(total)
    disk_used = get_readable_size(used)
    draw_progressbar(395, int(disk_percenatge))
    draw.text((335,302), f"( {disk_used} / {disk_total}, {disk_percenatge}% )", (255, 255, 255), font=IronFont)
                  
    ram_percentage = psutil.virtual_memory().percent
    ram_total = get_readable_size(psutil.virtual_memory().total)
    ram_used = get_readable_size(psutil.virtual_memory().used)	
    draw_progressbar(533, int(ram_percentage))
    draw.text((225,445), f"( {ram_used} / {ram_total} , {ram_percentage}% )", (255, 255, 255), font=IronFont)
    
    draw.text((335,600), f"{botuptime}", (255, 255, 255), font=IronFont)
    draw.text((857,607), f"{(end-start).microseconds/1000} ms", (255, 255, 255), font=IronFont)
    
    image.save("stats.png")
    await msg.edit_media(media=InputMediaPhoto("stats.png"))
    os.remove("stats.png")
	
     
