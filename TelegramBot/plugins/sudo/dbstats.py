from pyrogram import filters
from pyrogram.types import Message

from TelegramBot import bot
from TelegramBot.database import MongoDb
from TelegramBot.helpers.filters import sudo_cmd


@bot.on_message(filters.command("dbstats") & sudo_cmd)
async def dbstats(_, message: Message):
    """
    Returns database stats of MongoDB, which includes Total number
    of bot user and total number of bot chats.
    """

    TotalUsers = await mongodb.users.total_documents()
    TotalChats = await mongodb.chats.total_documents()

    stats_string = f"**Bot Database Statics.\n\n**Total Number of users = {TotalUsers}\nTotal number of chats  = {TotalChats}"
    return await message.reply_text(stats_string)
