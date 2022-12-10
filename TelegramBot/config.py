import json
from os import getenv
from dotenv import load_dotenv
load_dotenv("config.env") 

COMMAND_PREFIXES = dict(prefixes=json.loads(getenv("COMMAND_PREFIXES")))
prefixes = dict(prefixes=json.loads(getenv("COMMAND_PREFIXES")))

OWNER_USERID = json.loads(getenv("OWNER_USERID"))
SUDO_USERID = OWNER_USERID #owner is ultimately sudo user too

try:
  SUDO_USERID += json.loads(getenv("SUDO_USERID")) 
except: pass

BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

if "@" in BOT_USERNAME: BOT_USERNAME = BOT_USERNAME.replace("@", "")
