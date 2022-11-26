from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from beanie import PydanticObjectId

from models import messages as message_models

from services import messages as message_services

router = APIRouter()


@router.post('')
async def save_message(message: message_models.Message, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    return await message_services.save_message(message, Authorize)


@router.get('')
async def get_messages(query: message_models.MessageRetrieval, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    return await message_services.get_message(
        query.glove_address,
        Authorize
    )


@router.delete('/all')
async def delete_user_messages(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    return await message_services.delete_messages_user(Authorize)


@router.delete('/{id}')
async def delete_message_by_id(id: PydanticObjectId, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    return await message_services.delete_message_by_id(id, Authorize)


@router.delete('')
async def delete_messages_with_glove(query: message_models.MessageDeletion, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    return await message_services.delete_messages_glove(query.glove_address, Authorize)