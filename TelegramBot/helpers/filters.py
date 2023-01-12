"""
Creating custom filters 
https://docs.pyrogram.org/topics/create-filters
"""

from pyrogram import filters
from pyrogram.types import Message
from TelegramBot.config import SUDO_USERID, OWNER_USERID


def dev_users(_, __, message: Message) -> bool:
    return message.from_user.id in OWNER_USERID if message.from_user else False


def sudo_users(_, __, message: Message) -> bool:
    return message.from_user.id in SUDO_USERID if message.from_user else False


dev_cmd = filters.create(dev_users)
sudo_cmd = filters.create(sudo_users)
