from TelegramBot.helpers.decorators import dev_commands
from pyrogram.errors import MessageTooLong
from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup 
from TelegramBot.config import *
import httpx

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
commands = ["inspect", f"inspect@{BOT_USERNAME}"]
	
@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def inspect(client, message):
    
    try:
    	await message.reply_text(message, quote=True)
    except MessageTooLong:
    	output = await katbin_paste(message)
    	await message.reply_text(output, quote=True)
    
