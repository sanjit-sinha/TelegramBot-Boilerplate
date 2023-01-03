from motor.motor_asyncio import AsyncIOMotorClient 
from TelegramBot.logging import LOGGER 
from TelegramBot.config import MONGO_URI, prefixes 
from sys import exit as exiter


#from one string uri you can create multiple databases for different projects/bots. within each database you can store multiple collections, and within each collection you can store multiple documents.


class MongoDb:
    """
    MongoDb class to help with basic CRUD ( Create, Read, Delete, Update)
    operations of documents for a specific collection. 
    """
    
    def __init__(self, collection):
        self.collection = collection

    async def insert_document(self, document_data):
    	await self.collection.insert_one(document_data)

    async def create_document(self, document_data):
    	await self.collection.insert_one(document_data)
            
    async def read_document(self, document_id):
    	return await self.collection.find_one({"_id": document_id})
    	
    async def update_document(self, document_id , updated_data): 	
    	updated_data = {"$set": updated_data}    	
    	await self.collection.update_one({"_id": document_id}, updated_data)
    
    async def delete_document(self, document_id):
    	await self.collection.delete_one({'_id': document_id})
    	   
    async def total_documents(self):
    	"""
    	return total numner of documents in that collection. 
    	"""	
    	return await self.collection.count_documents({})
    
    async def get_all_id(self):
       """
       return list of all document "_id" in that collection. 
       """
       id_list = await self.collection.distinct("_id")
       return id_list
      
	
       
async def check_mongo_uri(MONGO_URI: str) -> None:
	try:
		mongo = AsyncIOMotorClient(MONGO_URI)
		await mongo.server_info()
	except:
		LOGGER(__name__).error(f"Error in Establishing connection with MongoDb URI. Please enter valid uri in the config section.")
		exiter(1)

		
		
#Initiating MongoDb motor client
mongodb = AsyncIOMotorClient(MONGO_URI) 

#Database Name (TelegramBot).
database = mongodb.TelegramBot 

#initiating collections from database TelegramBot.  
users = MongoDb(database.users)
chats = MongoDb(database.chats) 


