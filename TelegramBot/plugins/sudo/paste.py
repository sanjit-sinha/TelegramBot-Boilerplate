from TelegramBot.helpers.decorators import sudo_commands
from pyrogram import Client, filters
from pyrogram.types import Message
from TelegramBot.config import *
import re

prefixes = COMMAND_PREFIXES
paste_usage = f"**Usage:** Secretly tag the user(s) with some message. \n\n**Example:** /mention (@user1 @user2) your message"
commands = ["mention", f"mention@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
async def mention(client, message):
   """
   Secretly tag the user(s) with some message.
   """ 
   
   pattern_1 = "[^()]+"
   pattern_2 = '@[a-zA-Z0-9]+'
   	
   if len(message.command) < 2:
   	return await message.reply_text(paste_usage, quote=True)
   
   try: await message.delete()   	
   except: pass
   
   string = message.text.split(None, 1)[1]
   
   try:
   	content = re.findall(pattern_1, string)[1]	
   	usernames = re.findall(pattern_1, string)[0]
   	usernames_list = re.findall(pattern_2, usernames)
   	
   except Exception as e:
   	await message.reply_text(f"please follow proper format {e}" , quote=True)
   	
   userids_list = []
   for i in usernames_list:
       try: userid = await client.get_users(i) ; userids_list.append(userid.id)
       except: pass
   
   mention_msg = ''
   for i in userids_list: mention_msg+= f"[\u2063](tg://user?id={i})"  
   await message.reply_text(f"{content}{mention_msg}")
   
