from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TelegramBot.version import __python_version__, __version__, __pyro_version__, __license__
from pyrogram import Client, filters
from TelegramBot.config  import *


START_CAPTION="""**Hey there!! I am simple TelegramBot wich is made for the purpose for trying, testing, deploying and learnig about telegram bot using python pyrogram framework. \n\n Use buttons to navigate and know more about me :)**"""

COMMAND_CAPTION = """**Here are the list of commands wich you can use in bot.\n**"""

START_ANIMATION="https://telegra.ph/file/c0857672b427bec8542f6.mp4"

ABOUT_CAPTION = F"""• Python version : {__python_version__}
• Bot version : {__version__}
• pyrogram  version : {__pyro_version__}
• License : {__license__}

**Github Repo**: https://github.com/sanjit-sinha/Telegram-Bot-Boilerplate"""

USER_TEXT = """🗒️ Documentation for commands available to user's 
	
• /start: To Get this message
	
• /help: Alias command for start
	
• /alive: To check if bot is alive or not.

• /ping: Ping the telegram api server.
"""

SUDO_TEXT= """
🗒️ Documentation for Sudo Users commands.

• /speedtest: Check the internet speed of bot server.

• /serverstats: Get the stats of server.

• /stats: alias command for serverstats
"""

DEV_TEXT ="""
🗒️ Documentation for Developers Commands.
	
• /update: To update the bot to latest commit from repository. 

• /restart: Restart the bot.

• /log: To get the log file of bot.

• /shell: To run the terminal commands via bot.

• /exec: To run the python commands via bot
"""

  			  
START_BUTTON = [
    [
        InlineKeyboardButton("📖 Commands", callback_data="COMMAND_BUTTON"),
        InlineKeyboardButton("👨‍💻 About me", callback_data="ABOUT_BUTTON"),
    ],
    [InlineKeyboardButton("🔭 Original Repo", url=f"https://github.com/sanjit-sinha/Telegram-Bot-Boilerplate")],
]

	   	   
COMMAND_BUTTON = [
    [
        InlineKeyboardButton("Users", callback_data="USER_BUTTON"),
        InlineKeyboardButton("Sudo", callback_data="SUDO_BUTTON"),
    ],
    [InlineKeyboardButton("Developer", callback_data="DEV_BUTTON")],
    [InlineKeyboardButton("🔙 Go Back", callback_data="START_BUTTON")],
]


GOBACK_1_BUTTON = [[  InlineKeyboardButton("🔙 Go Back", callback_data="START_BUTTON") ]]  
          
GOBACK_2_BUTTON = [[ InlineKeyboardButton("🔙 Go Back", callback_data="COMMAND_BUTTON") ]] 
 	        

prefixes=COMMAND_PREFIXES 
commands=["start", f"start@{BOT_USERNAME}", "help", f"help@{BOT_USERNAME}"]
    	
@Client.on_message(filters.command(commands,**prefixes) & filters.private)
async def start(client, message):
     await message.reply_animation(animation=START_ANIMATION, caption=START_CAPTION,
                            reply_markup=InlineKeyboardMarkup(START_BUTTON))


@Client.on_callback_query()
async def botCallbacks(client, CallbackQuery):

		user_id = CallbackQuery.from_user.id
		
		if CallbackQuery.data =="ABOUT_BUTTON":
			await CallbackQuery.edit_message_text(ABOUT_CAPTION, reply_markup=InlineKeyboardMarkup(GOBACK_1_BUTTON))
			
		elif CallbackQuery.data =="START_BUTTON":
			await CallbackQuery.edit_message_text(START_CAPTION, reply_markup=InlineKeyboardMarkup(START_BUTTON))
			
		elif CallbackQuery.data =="COMMAND_BUTTON":
			await CallbackQuery.edit_message_text(COMMAND_CAPTION, reply_markup=InlineKeyboardMarkup(COMMAND_BUTTON))
			
		elif CallbackQuery.data =="USER_BUTTON":
			await CallbackQuery.edit_message_text(USER_TEXT, reply_markup=InlineKeyboardMarkup(GOBACK_2_BUTTON))
		
		elif CallbackQuery.data =="SUDO_BUTTON":
			if user_id not in SUDO_USERID:
				return await CallbackQuery.answer("You are not in the sudo user list.", show_alert=True)
			else:
				await CallbackQuery.edit_message_text(SUDO_TEXT, reply_markup=InlineKeyboardMarkup(GOBACK_2_BUTTON))
		
		elif CallbackQuery.data =="DEV_BUTTON":
			if user_id not in OWNER_USERID:
				return await CallbackQuery.answer("This is developer restricted command.", show_alert=True)
			else:
				await CallbackQuery.edit_message_text(DEV_TEXT, reply_markup=InlineKeyboardMarkup(GOBACK_2_BUTTON))

	
