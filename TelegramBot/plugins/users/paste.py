from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *
from bs4 import BeautifulSoup
import httpx
import aiofiles
import os 


async def katbin_paste(content):
	"""
	paste the text to katb.in website.
	"""
	
	katbin_url = "https://katb.in"
	client = httpx.AsyncClient()
	response = await client.get(katbin_url)
	
	soup = BeautifulSoup(response.content, "html.parser")
	csrf_token = soup.find('input', {"name":"_csrf_token"}).get("value")
	
	try:
		paste_post = await client.post(katbin_url, data={"_csrf_token":csrf_token, "paste[content]":content}, follow_redirects=False)
		output_url = f"{katbin_url}{paste_post.headers['location']}"
		await client.aclose()
		return output_url
	
	except: return "something went wrong while pasting text in katb.in."
	

prefixes = COMMAND_PREFIXES
paste_usage = f"**Usage:** paste the text to katb.in website. Reply to a text file, text message or just type the text after commamd.\n\n**Example:** /paste type your text"
commands = ["paste", f"paste@{BOT_USERNAME}", "p", f"p@{BOT_USERNAME}"]

@Client.on_message(filters.command(commands, **prefixes))
async def paste(client, message):
   """
   Paste the text to katb.in.
   """
   replied_message = message.reply_to_message   
   if len(message.command) > 1:
   	content = message.text.split(None, 1)[1]
     
   elif replied_message:
   		
   		if replied_message.text:
   			content = replied_message.text
   			   	  		   	
   		elif replied_message.document and any(format in replied_message.document.mime_type for format in ["text","json"]):		
   			await message.reply_to_message.download(os.path.join(os.getcwd(), "temp_file"))
   			async with aiofiles.open("temp_file", "r+") as file: content = await file.read()
   			os.remove("temp_file")
			
   		else: return await message.reply_text(paste_usage, quote=True)
      		
   elif len(message.command) < 2:
   	return await message.reply_text(paste_usage, quote=True)
   	 
   output = await katbin_paste(content)  
   return await message.reply_text(f"{output}", quote=True, disable_web_page_preview=True)
    
