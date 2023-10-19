from asyncio import sleep

from pyrogram import filters
from pyrogram.types import Message

from TelegramBot import bot
from TelegramBot.logging import LOGGER
from TelegramBot.database import MongoDb
from TelegramBot.helpers.filters import dev_cmd


@bot.on_message(filters.command(["broadcast"]) & dev_cmd)
async def broadcast(_, message: Message):
    """Broadcast the message via bot to bot users and groups.."""

    if not (broadcast_msg := message.reply_to_message):
        broadcast_usage = "Reply with command /broadcast to the message you want to broadcast.\n\n/broadcast users - To broadcast message to users only.\n\n/broadcast chats - To broadcast message to chats only.\n\n/broadcast all - To broadcast message everywhere."
        return await message.reply_text(broadcast_usage, quote=True)

    proses_msg = await message.reply_text(
        "**Broadcasting started. Please wait for few minutes for it to get completed.", quote=True)

    to_chats = False
    to_users = False
    disable_notification = True
    commands = message.command

    if len(commands) > 3:
        return await proses_msg.edit("Invalid Command")

    for command in message.command:
        if command.lower() == "all":
            to_chats = True
            to_users = True
        elif command.lower() == "users":
            to_users = True
            to_chats = False
        elif command.lower() == "chats":
            to_users = False
            to_chats = True
        elif command.lower() == "loud":
            disable_notification = False

    total_list = []
    if to_chats:
        total_list += await MongoDb.chats.get_all_id()

    if to_users:
        total_list += await MongoDb.users.get_all_id()

    failed = 0
    success = 0

    for __id in total_list:
        try:
            await broadcast_msg.copy(
                __id, broadcast_msg.caption, disable_notification=disable_notification)
            success += 1
            # preventing flood wait
            await sleep(0.3)
        except Exception as error:
            LOGGER(__name__).error(str(error))
            failed += 1

    return await proses_msg.edit(
        f"**The message has been successfully broadcasted.**\n\nTotal success = {success}\nTotal Failure = {failed}")
