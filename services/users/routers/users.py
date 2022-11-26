from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from models import users as users_models

from services import users as user_services

router = APIRouter()


@router.post('/signup')
async def register(user: users_models.UserRegister, Authorize: AuthJWT = Depends()):
    return await user_services.register_service(user, Authorize)


@router.post('/signin')
async def login(user: users_models.UserLogin, Authorize: AuthJWT = Depends()):
    return await user_services.login_service(user, Authorize)


@router.post('/refresh')
async def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    return await user_services.refresh_service(Authorize)
