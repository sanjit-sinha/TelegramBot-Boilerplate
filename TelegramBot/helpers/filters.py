"""
Creating custom filters 
https://docs.pyrogram.org/topics/create-filters
"""

from pyrogram import filters
from pyrogram.types import Message
from TelegramBot.config import SUDO_USERID,  OWNER_USERID 


def dev_users(_, __, message: Message) -> bool:
    if not message.from_user:
        return False
    return message.from_user.id == OWNER_USERID
    
    
def sudo_users(_, __, message: Message) -> bool:
    if not message.from_user:
        return False
    return message.from_user.id == SUDO_USERID 


dev_cmd  = filters.create(dev_users)
sudo_cmd = filters.create(sudo_users)
