import os

from beanie import init_beanie
import motor.motor_asyncio

from schemas import users as user_schemas

async def init_db():
    db_user = os.getenv('DB_USER', None)
    db_pass = os.getenv('DB_PASS', None)
    
    print(db_user, db_pass, sep=' -- ')

    if db_user is None or db_pass is None:
        raise ValueError('Value of db_user and db_pass cannot be None.')

    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{db_user}:{db_pass}@mongodb:27017"
    )

    await init_beanie(database=client.unihack, document_models=[user_schemas.User])
