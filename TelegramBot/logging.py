import logging
import os
from logging.handlers import RotatingFileHandler

# Removing old log files if they exist and starting logging from a fresh file.
if os.path.exists("logs.txt"):
    os.remove("logs.txt")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", mode="w+", maxBytes=5000000, backupCount=3),
        logging.StreamHandler(),
    ]
)

# Suppressing pyrogram INFO messages.
logging.getLogger("pyrogram").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
