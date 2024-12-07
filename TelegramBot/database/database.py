from typing import Union
from datetime import datetime

from pyrogram.types import Message
from TelegramBot.database.MongoDb import users, chats


async def save_user(user: Message) -> None:
    """Saves the new user id in the database if it is not already there."""

    insert_format = {
        "name": (user.first_name or " ") + (user.last_name or ""),
        "username": user.username,
        "date": datetime.now(),
    }

    return await users.update_document(user.id, insert_format)


async def save_chat(chatid: Union[int, str]) -> None:
    """Save the new chat id in the database if it is not already there."""

    insert_format = {"date": datetime.now()}
    return await chats.update_document(chatid, insert_format)
