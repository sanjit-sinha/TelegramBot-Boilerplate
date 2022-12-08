from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TelegramBot.helpers.decorators import dev_commands
from TelegramBot.logging import LOGGER
from pyrogram import Client, filters
from TelegramBot import bot
from pyrogram.types import Message
from TelegramBot.config import *
from io import StringIO, BytesIO
import aiofiles
import subprocess
import traceback
import sys
import os


prefixes = COMMAND_PREFIXES

shell_usage = f"**USAGE:** Executes terminal commands directly via bot.\n\n<pre>/shell pip install requests</pre>"
commands = ["shell", f"shell@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def shell(client, message: Message):
    """
    Executes terminal commands via bot.
    """
    if len(message.command) < 2:
        return await message.reply_text(shell_usage, quote=True)

    user_input = message.text.split(None, 1)[1].split(" ")

    try:
        shell = subprocess.Popen(
            user_input, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        stdout, stderr = shell.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    except Exception as error:
        LOGGER(__name__).warning(f"{error}")
        return await message.reply_text(f"**Error**:\n\n{error}", quote=True)

    if len(result) > 2000:
        file = BytesIO(result.encode())
        file.name = "output.txt"
        await message.reply_text("output too large. sending it as a file..", quote=True)
        await client.send_document(message.chat.id, file, caption=file.name)
    else:
        await message.reply_text(f"**Output:**:\n\n{result}", quote=True)














exec_usage = f"**USAGE:** Executes python commands directly via bot.\n\n<pre>/exec print('hello world')</pre>"
commands = ["exec", f"exec@{BOT_USERNAME}", "execute"]


async def aexec(code, client, message):
    exec("async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n")))
        
    return await locals()["__aexec"](client, message)


#refresh_button = [[InlineKeyboardButton("refresh", callback_data="COMMAND_BUTTON")]]

#reply_markup=InlineKeyboardMarkup(refresh_button),

async def exec(client, message):        
    if len(message.command) < 2:
        return await message.reply_text(exec_usage)
        
    code = message.text.split(None, 1)[1]

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None

    try: await aexec(code, client, message)
    except Exception: exc = traceback.format_exc()

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
    final_output = f"**output**: \n\n{evaluation.strip()}"
    
    
    if len(final_output) > 2000:
        async with aiofiles.open("output.txt", "w+", encoding="utf8") as file:
            await file.write(str(evaluation.strip()))
        await message.reply_text("output too large. sending it as a file..", quote=True)
        await client.send_document(message.chat.id, "output.txt", caption="output.txt")
        os.remove("output.txt")
    
    else:
    	await message.reply_text(final_output, quote=True)


@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def executor(client, message):
    await exec(client, message)
    
    
  
    
    
