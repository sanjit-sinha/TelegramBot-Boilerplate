from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TelegramBot.helpers.decorators import dev_commands
from pyrogram.errors import MessageNotModified
from TelegramBot.logging import LOGGER
from pyrogram import Client, filters
from pyrogram.types import Message
from io import StringIO, BytesIO
from TelegramBot.config import *
from TelegramBot import bot
import subprocess
import traceback
import aiofiles
import asyncio
import shlex
import sys
import os


shell_usage = f"**USAGE:** Executes terminal commands directly via bot.\n\n**Example: **<pre>/shell pip install requests</pre>"
commands = ["shell", "sh"]

@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def shell(client: Client, message: Message):
    """
    Executes command in terminal via bot.
    """
    
    if len(message.command) < 2:
        return await message.reply_text(shell_usage, quote=True)

    user_input = message.text.split(None, 1)[1]
    args = shlex.split(user_input)
    
    try:
        shell_replymsg = await message.reply_text("running...", quote=True)    
        shell = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await shell.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    except Exception as error:
        LOGGER(__name__).warning(f"{error}")
        return await shell_replymsg.edit(f"Error :-\n\n{error}")

    if len(result) > 4000:
        file = BytesIO(result.encode())
        file.name = "output.txt"
        await shell_replymsg.edit("output too large. sending it as a file..")
        await client.send_document(message.chat.id, file, caption=file.name)
    else:
        await shell_replymsg.edit(f"Output :-\n\n{result}")



	
	
exec_usage = f"**Usage:** Executes python commands directly via bot.\n\n**Example: **<pre>/exec print('hello world')</pre>"
commands = ["exec", "py"]

async def aexec(code, client, message):
    exec("async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n")))        
    return await locals()["__aexec"](client, message)
    
async def py_runexec(client, message, replymsg):
 
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    
    try:
    	await replymsg.edit("executing...") 	    
    	code = message.text.split(None, 1)[1]  	
    except IndexError:
    	return await replymsg.edit("No codes found to execute.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Refresh  🔄", callback_data="refresh")]]))
    	
    if "config.env" in code:
        return await replymsg.edit("That's a dangerous operation! Not Permitted!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Refresh  🔄",  callback_data="refresh")]]))
                                            
    try:
    	await aexec(code, client, message)
    except Exception:
    	exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
 
    evaluation = ""
    if exc:
    	evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "success" 
    final_output = f"{evaluation.strip()}"    

        
    if len(final_output) > 4000:
        async with aiofiles.open("output.txt", "w+", encoding="utf8") as file:
            await file.write(str(evaluation.strip()))
       
        await replymsg.edit("output too large. sending it as a file...",  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("refresh 🔄",callback_data="refresh")]]))
        await client.send_document(message.chat.id, "output.txt", caption="output.txt")
        os.remove("output.txt")
    
    else:
    	return await replymsg.edit(final_output,  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("refresh 🔄",callback_data="refresh")]]))


@Client.on_callback_query(filters.regex("refresh"))
async def botCallbacks(client, CallbackQuery):
    
    cliker_user_id = CallbackQuery.from_user.id
    message_user_id = CallbackQuery.message.reply_to_message.from_user.id
    
    if cliker_user_id != message_user_id:
    	return await CallbackQuery.answer("That command is not initiated by you.", show_alert=True )

    message  = await client.get_messages(CallbackQuery.message.chat.id,CallbackQuery.message.reply_to_message.id)	    
    replymsg = await client.get_messages(CallbackQuery.message.chat.id, CallbackQuery.message.id)

    if CallbackQuery.data == "refresh":
        await py_runexec(client, message, replymsg)
  
  
@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def py_exec(client, message):
	"""
	Executes python command via bot with refresh button.
	"""
	
	if len(message.command) < 2:
		await message.reply_text(exec_usage)				
	else:
	   replymsg = await message.reply_text("executing..", quote=True)
	   await py_runexec(client, message, replymsg)
    
    


