from TelegramBot.database import MongoDb as db
from datetime import datetime, timezone


async def saveUser(user):
    """_summary_

    Args:
        user (_type_): _description_
    """

    insert_format = {
        "name": (user.first_name or " ") + (user.last_name or ""),
        "username": user.username,
        "date": datetime.now(timezone.utc),
    }
    await db.users.update_document(user.id, insert_format)


async def saveChat(chatid):
    insert_format = {"date": datetime.now(timezone.utc)}
    await db.chats.update_document(chatid, insert_format)
