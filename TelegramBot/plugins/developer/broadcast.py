from TelegramBot.database import MongoDb
from TelegramBot.helpers.decorators import *
from TelegramBot.config import *
from pyrogram import Client, filters
import asyncio


commands = ["broadcast"]
broadcast_usage = f"**Usage:** Broadcast the message to all users as well as chats wich are saved in database.\n\n/broadcast type your message\n\nuse the flag '-all' to send broadcast message to both users as well as chats.\n\n/broadcast -all type your message."

@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
@ratelimiter
async def broadcast(client, message):
   """
   Broadcast the message via bot.
   """
   if len(message.command) < 2:
       return await message.reply_text(broadcast_usage, quote=True)
   else:
       user_message =  message.text.split(None, 1)[1]
   
   broadcast_msg = await message.reply_text("**Broadcasting started. Please wait for few minutes to get completed.")
   total_list = []
   
   if "-all" in user_message:
       user_message = user_message.replace("-all", "")
       total_list += await MongoDb.chats.get_all_id()
   
   total_list += await MongoDb.users.get_all_id()	
   	   
   failed = 0
   success = 0
   
   for id in total_list:
   	try:
   		await client.send_message(chat_id=id, text=user_message)
   		success += 1
         
         #prevent flood.
         await asyncio.sleep(4)
   	except Exception as error:
   		failed += 1
   	
   return await broadcast_msg.edit(f"**Successfully Broadcasted Message.**\n\nTotal sucess = {success}\nTotal Failure = {failed}")
   
   
 
