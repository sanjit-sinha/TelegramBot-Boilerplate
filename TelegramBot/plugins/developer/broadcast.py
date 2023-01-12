from asyncio import sleep, gather

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from TelegramBot.database import MongoDb
from TelegramBot.helpers.decorators import ratelimiter
from TelegramBot.helpers.filters import dev_cmd
from TelegramBot.logging import LOGGER


@Client.on_message(filters.command(["broadcast"]) & dev_cmd)
@ratelimiter
async def broadcast(client: Client, message: Message):
    """
    Broadcast the message via bot to bot users and groups..
    """

    if not (broadcast_msg := message.reply_to_message):
        broadcast_usage = f"**Usage:** Broadcast the message to all users as well as chats witch are saved in database.\n\n/broadcast type your message\n\nuse the flag '-all' to send broadcast message to both users as well as chats.\n\n/broadcast -all type your message."
        return await message.reply_text(broadcast_usage, quote=True)

    proses_msg = await message.reply_text(
        "**Broadcasting started. Please wait for few minutes for it to get completed.",
        quote=True,
    )

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

    if not all([to_users, to_chats]):
        to_users = True
    if to_users:
        total_list += await MongoDb.users.get_all_id()

    list_f = [
        _sending_broadcast(broadcast_msg, disable_notification, __id)
        for __id in total_list
    ]
    tasks = gather(*list_f, return_exceptions=True)
    results = await tasks
    success = 0
    failed = 0
    for result in results:
        if result == "success":
            success += 1
        else:
            failed += 1
    return await proses_msg.edit(
        f"**The message has been successfully broadcasted.**\n\nTotal success = {success}\nTotal Failure = {failed}"
    )


async def _sending_broadcast(broadcast_msg, disable_notification, __id):
    try:
        await broadcast_msg.copy(
            __id, broadcast_msg.caption, disable_notification=disable_notification
        )
        return "success"
    except FloodWait as flood:
        await sleep(flood.value)
        return await _sending_broadcast(broadcast_msg, disable_notification, __id)
    except Exception as e:
        LOGGER(__name__).error(str(e))
        return "failed"
