import hashlib

from models import users as users_models
from schemas import users as users_schemas


async def create_user(user: users_models.UserRegister) -> dict:
    return await users_schemas.User(
        username=user.username,
        email=user.email,
        password=hashlib.sha256(bytes(user.password, 'utf-8')).hexdigest()
    ).create()
