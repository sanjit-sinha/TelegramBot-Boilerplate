from sys import exit as exiter

from motor.motor_asyncio import AsyncIOMotorClient

from TelegramBot.config import MONGO_URI
from TelegramBot.logging import LOGGER


# from one string uri you can create multiple databases for different projects/bots. within each database you can store multiple collections, and within each collection you can store multiple documents.


class MongoDb:
    """
    MongoDb class to help with basic CRUD ( Create, Read, Delete, Update)
    operations of documents for a specific collection. 
    """

    def __init__(self, collection):
        self.collection = collection

    async def read_document(self, document_id):
        """
        Read the document using document_id.
        """
        return await self.collection.find_one({"_id": document_id})

    async def update_document(self, document_id, updated_data):
        """
        Update as well as create document from document_id.
        """
        updated_data = {"$set": updated_data}
        await self.collection.update_one({"_id": document_id}, updated_data, upsert=True)

    async def delete_document(self, document_id):
        """
        Delete the document using document_id from collection.
        """
        await self.collection.delete_one({'_id': document_id})

    async def total_documents(self):
        """
        Return total number of documents in that collection.
        """
        return await self.collection.count_documents({})

    async def get_all_id(self):
        """
        Return list of all document "_id" in that collection.
        """
        return await self.collection.distinct("_id")


async def check_mongo_uri(MONGO_URI: str) -> None:
    try:
        mongo = AsyncIOMotorClient(MONGO_URI)
        await mongo.server_info()
    except:
        LOGGER(__name__).error(
            "Error in Establishing connection with MongoDb URI. Please enter valid uri in the config section.")
        exiter(1)


# Initiating MongoDb motor client
mongodb = AsyncIOMotorClient(MONGO_URI)

# Database Name (TelegramBot).
database = mongodb.TelegramBot

# initiating collections from database TelegramBot.
users = MongoDb(database.users)
chats = MongoDb(database.chats)
