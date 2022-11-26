import hashlib

from fastapi import HTTPException, status

from models import users as users_models
from schemas import users as users_schemas


async def create_user(user: users_models.UserRegister) -> dict:
    return await users_schemas.User(
        username=user.username,
        email=user.email,
        password=hashlib.sha256(bytes(user.password, 'utf-8')).hexdigest()
    ).create()


async def validate_user(user: users_models.UserLogin) -> bool:
    potential = await users_schemas.User.find_one(users_schemas.User.username == user.username)

    if potential:
        return hashlib.sha256(bytes(user.password, 'utf-8')).hexdigest() == potential.password
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={'detail': 'User with this username not found!'}
    )