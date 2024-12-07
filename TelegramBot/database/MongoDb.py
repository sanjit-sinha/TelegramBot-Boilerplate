import sys
from typing import Union
from motor.motor_asyncio import AsyncIOMotorClient

from TelegramBot.logging import LOGGER
from TelegramBot.config import MONGO_URI


"""
from one String URI you can create multiple databases for different projects/bots.
within each database you can store multiple collections, and within each collection
you can store multiple documents.

String URI
│
└── database_one (Project One)
│   ├── collection_one  (list of users)
│   │   ├──document_one (user_one)
│   │   └──document_two (user_two)
│   │
│   └── collection_two (list of chats)
│        ├──document_one (chat_one)
│        └──document_two (chat_two)
│
└── database_one (Project Two)
    ├── collection_one
    │   ├──document_one
    │   └──document_two
    │
    └── collection_two
        ├──document_one
        └──document_two

Up above is a tree like structure of database which explains how data is stored in mongoDB.
"""


class MongoDB:
    """
    MongoDb class to help with basic CRUD ( Create, Read, Delete, Update)
    operations of documents for a specific collection.
    """

    def __init__(self, collection: str):
        self.collection: str = collection

    async def read_document(
        self, document_id: Union[str, int], projection=None
    ) -> dict:
        """
        Read document from collection using document_id.
        If projection is given, it will return only the given fields.

        Example:
        projection = {"_id": 0, "name": 1, "age": 1}
        # https://www.geeksforgeeks.org/mongodb-projection/
        """

        if projection:
            return await self.collection.find_one({"_id": document_id}, projection)

        return await self.collection.find_one({"_id": document_id})

    async def update_document(
        self, document_id: Union[str, int], updated_data: dict
    ) -> None:
        """Updates as well as create document using mongodb document_id from collection."""

        updated_data = {"$set": updated_data}
        await self.collection.update_one(
            {"_id": document_id}, updated_data, upsert=True
        )

    async def delete_document(self, document_id: Union[str, int]) -> None:
        """Delete the document using document_id using mongodb document_id from collection."""

        await self.collection.delete_one({"_id": document_id})

    async def total_documents(self) -> int:
        """Return total number of mongodb documents in current collection."""

        return await self.collection.count_documents({})

    async def get_all_id(self) -> list:
        """Return list of all mongodb document "_id" in current collection."""

        return await self.collection.distinct("_id")


async def check_mongo_uri(MONGO_URI: str) -> None:
    try:
        mongo = AsyncIOMotorClient(MONGO_URI)
        await mongo.server_info()
    except:
        LOGGER(__name__).error(
            "Error in Establishing connection with MongoDb URI. Please enter valid uri in the config section."
        )
        sys.exit(1)


# Initiating MongoDb motor client
mongodb = AsyncIOMotorClient(MONGO_URI)

# Database Name (TelegramBot).
database = mongodb.TelegramBot

# Initiating different collections from database TelegramBot.
users = MongoDB(database.users)
chats = MongoDB(database.chats)
