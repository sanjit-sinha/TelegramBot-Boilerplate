import logging
import os
from logging.handlers import RotatingFileHandler

#removing old logs file if they exist.
try: os.remove("logs.txt")
except: pass
    
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", mode="w+", maxBytes=5000000, backupCount=10),
        logging.StreamHandler()])

logging.getLogger("pyrogram").setLevel(logging.ERROR)
def LOGGER(name: str) -> logging.Logger:
    """_summary_

    Args:
        name (str): _description_

    Returns:
        logging.Logger: _description_
    """
    return logging.getLogger(name)
