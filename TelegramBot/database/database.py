from TelegramBot.database.MongoDb import *
from datetime import datetime


async def saveUser(user):
    """
    Saves new user in the database if they start the bot.
    """
    format = {
            '_id': user.id,
            'name': (user.first_name or " ") + (user.last_name or ""),
            'username': user.username,
            'date': str(datetime.now().date())
    }
        	
    if not await users.read_document(document_id = user.id):
        await users.insert_document(format)

        
async def saveChat(chatid):
    """
    Saves new group in the database if bot is added in new group.
    """
    print("test")
    format = {
           '_id': chatid,
           'date': str(datetime.now().date())    
    }
    
    if not await chats.read_document(document_id = chatid):
        await chats.insert_document(format)
