from fastapi import HTTPException, status
from fastapi_jwt_auth import AuthJWT

from db import messages as message_crud
from schemas import messages as message_schemas
from models import messages as message_models

from beanie import PydanticObjectId


async def save_message(message: message_models.Message, Authorize: AuthJWT):
    Authorize.jwt_required()

    user = Authorize.get_jwt_subject()
    data = message_schemas.Message(
        username=user,
        glove_address=message.glove_address,
        is_phone=message.is_phone,
        message=message.message
    )
    return await message_crud.save_message(data)


async def get_messages(glove_address: str, Authorize: AuthJWT):
    Authorize.jwt_required()

    user = Authorize.get_jwt_subject()
    return await message_crud.get_messages(user, glove_address)


async def delete_messages_user(Authorize: AuthJWT):
    Authorize.jwt_required()

    user = Authorize.get_jwt_subject()
    try:
        await message_crud.delete_messages_user(user)
    except Exception as exc: 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'detail': f'Error occurred while trying to delete {str(exc)}'}
        )


async def delete_message_by_id(id: PydanticObjectId, Authorize: AuthJWT):
    Authorize.jwt_required()

    user = Authorize.get_jwt_subject()
    try:
        await message_crud.delete_message_by_id(user, id)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'detail': f'Error occurred while trying to delete {str(exc)}'}
        )


async def delete_messages_glove(glove_address: str, Authorize: AuthJWT):
    Authorize.jwt_required()

    user = Authorize.get_jwt_subject()
    try:
        await message_crud.delete_messages_glove(user, glove_address)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'detail': f'Error occurred while trying to delete {str(exc)}'}
        )
    