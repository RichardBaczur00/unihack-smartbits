from fastapi import HTTPException, status
from fastapi_jwt_auth import AuthJWT

from models import users as user_models
from schemas import users as user_schemas
from db import users as users_crud


async def generate_tokens(username: str, Authorize: AuthJWT):
    access_token = Authorize.create_access_token(subject=username)
    refresh_token = Authorize.create_refresh_token(subject=username)

    return { 'access_token': access_token, 'refresh_token': refresh_token }


async def register_service(user: user_models.UserRegister, Authorize: AuthJWT):
    await users_crud.create_user(user)
    return await generate_tokens(user.username, Authorize)


async def login_service(user: user_models.UserLogin, Authorize: AuthJWT):
    if await users_crud.validate_user(user):
        return await generate_tokens(user.username, Authorize)
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={'detail': 'Wrong user or password'}
    )


async def refresh_service(Authorize: AuthJWT):
    return {
        'access_token': Authorize.create_access_token(
            subject=Authorize.get_jwt_subject(), fresh=True
        )
    }
