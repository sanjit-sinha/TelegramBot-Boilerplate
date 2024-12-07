import os
import aiofiles

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from TelegramBot import bot
from TelegramBot.helpers.filters import is_ratelimited
from TelegramBot.helpers.pasting_services import katbin_paste


@bot.on_message(filters.command("paste") & is_ratelimited)
async def paste(_, message: Message):
    """Pastes given text on the Katb.in website."""

    paste_usage = "**Usage:** Paste the text on the katb.in website. Reply to a text file, \
    text message or just type the text after command.\n\n**Example:** /paste type your text"

    paste_reply = await message.reply_text("pasting...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif replied_message:
        if replied_message.text:
            content = replied_message.text

        elif replied_message.document and any(
            format in replied_message.document.mime_type for format in {"text", "json"}
        ):

            file_path = await replied_message.download()
            async with aiofiles.open(file_path, "r+") as file:
                content = await file.read()
            os.remove(file_path)

        else:
            return await paste_reply.edit(paste_usage)

    elif len(message.command) < 2:
        return await paste_reply.edit(paste_usage)

    output = await katbin_paste(content)
    button = [[InlineKeyboardButton(text="Paste Link 🔗", url=output)]]

    return await paste_reply.edit(
        text=output,
        reply_markup=InlineKeyboardMarkup(button),
        disable_web_page_preview=True)
