"""
https://github.com/UsergeTeam/Userge/blob/alpha/userge/logger.py
"""

import logging
from logging.handlers import RotatingFileHandler
import os

try: os.remove("logs.txt")
except: pass
    
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", mode="w+", maxBytes=5000000, backupCount=10),
        logging.StreamHandler()
    ]
)

#logging.getLogger("pyrogram").setLevel(logging.ERROR)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
