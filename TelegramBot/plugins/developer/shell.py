import os
import asyncio
from io import BytesIO

from pyrogram import filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

from TelegramBot import bot
from TelegramBot.logging import LOGGER
from TelegramBot.helpers.filters import dev_cmd


@bot.on_callback_query(filters.regex("shellcallback_"))
async def shell_callback(_, callback: CallbackQuery):
    """Callback for shell command."""

    if callback.from_user.id != callback.message.reply_to_message.from_user.id:
        return await callback.answer(
            "That command is not initiated by you.", show_alert=True)

    process_id = callback.data.split("_")[-1]
    message = callback.message

    return await message.edit(f"Process ID: {process_id} Killed Successfully.")


@bot.on_message(filters.command(["shell", "sh"]) & dev_cmd)
async def shell_executor(_, message: Message):
    """Executes command in terminal via bot."""

    if len(message.command) < 2:
        shell_usage = "**USAGE:** Executes commands directly in terminal shell via bot.\n\n**Example: **<pre>/shell pip install requests</pre>"
        return await message.reply_text(shell_usage, quote=True)

    user_input = message.text.split(maxsplit=1)[1]

    try:
        shell = await asyncio.create_subprocess_shell(
            user_input,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            preexec_fn=os.setsid)

        button = [[InlineKeyboardButton("Kill Process", callback_data=f"shellcallback_{shell.pid}")]]
        shell_replymsg = await message.reply_text(
            "Executing...", reply_markup=InlineKeyboardMarkup(button), quote=True)

        stdout, stderr = await shell.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    except Exception as error:
        LOGGER(__name__).warning(f"{error}")
        return await shell_replymsg.edit(f"--**Error**--\n\n`{error}`")

    if len(result) > 4000:
        await shell_replymsg.edit("output too large. sending it as a file...")
        file = BytesIO(result.encode())
        file.name = "output.txt"
        await shell_replymsg.reply_document(
            file, caption=f"shell command :- `{user_input}`", quote=True)
    else:
        await shell_replymsg.edit(f"--**Output**--\n\n`{result}`")
