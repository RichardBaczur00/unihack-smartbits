from fastapi import APIRouter
from fastapi_jwt_auth import AuthJWT

from services import speech as speech_services


router = APIRouter()


@router.get('/{id}/')
async def convert_message_by_id(Authorize: AuthJWT):
    raise NotImplementedError


@router.get('')
async def convert_message_on_the_fly(message: str, Authorize: AuthJWT):
    raise NotImplementedError