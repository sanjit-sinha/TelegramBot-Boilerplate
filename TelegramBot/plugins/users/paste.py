
from TelegramBot.helpers.functions import get_readable_time    
from pyrogram import Client, filters
from TelegramBot import BotStartTime
from pyrogram.types import Message
from TelegramBot.config import *
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import os 

prefixes = COMMAND_PREFIXES
paste_usage = f"**Usage:** paste the text to katb.in website. Reply to a text file, text message or just type the text after commamd.\n\n**Example:** <pre>/paste type your text</pre>"
commands = ["paste", f"paste@{BOT_USERNAME}", "p", f"p@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
async def paste(client, message):
   """
   Paste the text to katb.in.
   """
   
   replied_message = message.reply_to_message
   if replied_message:
   		if replied_message.text:
   			content = replied_message.text   	
   	
   		elif replied_message.document and "text" in replied_message.document.mime_type:		
   			await message.reply_to_message.download(os.path.join(os.getcwd(), "temp_file"))
   			with open("temp_file", "r+") as file: content = file.read()
   			os.remove("temp_file")
			
   		else: return await message.reply_text(paste_usage, quote=True)
   
   elif len(message.command) > 1:
   	content = message.text.split(None, 1)[1]
   	
   elif len(message.command) < 2:
   	return await message.reply_text(paste_usage, quote=True)
   	 
   output = await katbin_paste(content)  
   return await message.reply_text(f"{output}", quote=True, disable_web_page_preview=True)
   


async def katbin_paste(content):
	katbin_url = "https://katb.in"
	client = requests.Session()
	response = client.get(katbin_url)
	
	soup = BeautifulSoup(response.content, "html.parser")
	csrf_token = soup.find('input', {"name":"_csrf_token"}).get("value")
	
	try:
		paste_post = client.post(katbin_url, data={"_csrf_token":csrf_token, "paste[content]":content}, allow_redirects=False)
		output_url = f"{katbin_url}{paste_post.headers['location']}"
		return output_url
	
	except:
		return "something went wrong while pasting text in katb.in."
	

   
