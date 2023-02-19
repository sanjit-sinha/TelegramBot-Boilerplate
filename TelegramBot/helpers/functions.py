from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.types import Message

from TelegramBot.config import SUDO_USERID
from typing import Union 


async def isAdmin(message: Message) -> bool:
    """
    Return True if the message is from owner or admin of the group or sudo of the bot.
    """

    if not message.from_user:
        return
    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
        return

    user_id = message.from_user.id
    if user_id in SUDO_USERID:
        return True

    check_status = await message.chat.get_member(user_id)
    return check_status.status in [ChatMemberStatus.OWNER,ChatMemberStatus.ADMINISTRATOR]


def get_readable_bytes(size: Union[int, str]) -> str:
    """
    Return a human readable file size from bytes.
    """

    UNIT_SUFFIXES = ['B', 'KiB', 'MiB', 'GiB', 'TiB']

    if isinstance(size, str):
        size = int(size)

    if size < 0:
        raise ValueError('Size must be positive')
    if size == 0:
        return '0 B'

    i = 0
    while size >= 1024 and i < len(UNIT_SUFFIXES) - 1:
        size /= 1024
        i += 1

    return f"{size:.2f} {UNIT_SUFFIXES[i]}"
      
    
def get_readable_bytes(size: str) -> str:
    """
    Return a human readable file size from bytes.
    """

    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}

    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0

    while size > power:
        size /= power
        raised_to_pow += 1

    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}B"
