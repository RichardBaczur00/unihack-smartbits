from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from fastapi_jwt_auth import AuthJWT

from services import speech as speech_services


router = APIRouter()


@router.get('/{id}/')
async def convert_message_by_id(Authorize: AuthJWT = Depends()):
    raise NotImplementedError


@router.get('')
async def convert_message_on_the_fly(message: str, Authorize: AuthJWT = Depends()):
    id = await speech_services.save_audio_to_tmp(message)
    return FileResponse(f'./tmp/{id}.mp3')