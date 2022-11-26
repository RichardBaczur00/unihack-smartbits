from fastapi_jwt_auth import AuthJWT

from beanie import PydanticObjectId
from schemas import messages as message_schemas


async def save_message(message: message_schemas.Message):
    return await message.create()
    

async def get_messages(username: str, glove_address: str):
    return await message_schemas.Message.find(
        message_schemas.Message.username == username and \
        message_schemas.Message.glove_address == glove_address
    ).to_list()


async def delete_messages_user(username: str):
    await message_schemas.Message.find(
        message_schemas.Message.username == username
    ).delete()


async def delete_message_by_id(username: str, id: PydanticObjectId):
    await message_schemas.Message.find_one(
        message_schemas.Message.id == id
    ).delete()


async def delete_message_glove(username: str, glove_address: str):
    await message_schemas.Message.find(
        message_schemas.Message.username == username,
        message_schemas.Message.glove_address == glove_address
    ).delete()