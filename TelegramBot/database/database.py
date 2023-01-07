from TelegramBot.database import MongoDb as db
from datetime import datetime


async def saveUser(user):
    """
    Saves new user in the database if they start the bot.
    """
    
    insert_format = {
            '_id': user.id,
            'name': (user.first_name or " ") + (user.last_name or ""),
            'username': user.username,
            'date': str(datetime.now().date())
    }
        	
    if not await db.users.read_document(document_id = user.id):
        await db.users.insert_document(insert_format)

        
async def saveChat(chatid):
    """
    Saves new group in the database if bot is added in new group.
    """
  
    insert_format = {
           '_id': chatid,
           'date': str(datetime.now().date())    
    }
    
    if not await db.chats.read_document(document_id = chatid):
        await db.chats.insert_document(insert_format)
