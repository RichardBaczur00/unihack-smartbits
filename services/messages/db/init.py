from beanie import init_beanie
import motor.motor_asyncio

from schemas import users as user_schemas

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://mongodb:27017/unihack"
    )

    await init_beanie(database=client.db_name, document_models=[user_schemas.User])