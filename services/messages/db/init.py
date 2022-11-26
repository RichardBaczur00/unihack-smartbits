from beanie import init_beanie
import motor.motor_asyncio

from schemas import messages as message_schemas

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://mongodb:27017/unihack"
    )

    await init_beanie(database=client.db_name, document_models=[message_schemas.Message])