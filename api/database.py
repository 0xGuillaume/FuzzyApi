import motor.motor_asyncio
from .models import FooModel


MONGODB_URL = "mongodb://root:root@mongo:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.fuzzy


async def fetch_foos():
    """Fetch all foos"""

    documents = []
    cursor = database.foo.find({})

    async for document in cursor:
        documents.append(FooModel(**document))

    return documents


async def fetch_foo(id):
    """Fetch one specifid foo (by id)"""

    document = await database.foo.find_one({"title": id})

    return document
