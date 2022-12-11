from TelegramBot.helpers.pasting_services import katbin_paste
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *
import aiofiles
import os 


commands = ["paste", "p"]
paste_usage = f"**Usage:** paste the text to katb.in website. Reply to a text file, text message or just type the text after commamd.\n\n**Example:** /paste type your text"

@Client.on_message(filters.command(commands, **prefixes))
async def paste(client, message):
   """
   Paste the text to katb.in website.
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
   	
   paste_reply = await message.reply_text("pasting...", quote=True)
   	 
   output = await katbin_paste(content)  
   return await paste_reply.edit(f"{output}", disable_web_page_preview=True)
    
