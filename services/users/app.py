import os

from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from db import init

from routers.users import router as user_router


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv('JWT_SECRET', 'secret')


@AuthJWT.load_config
def get_config():
    return Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app = FastAPI(openapi_url='/api/v1/users/openapi.json', docs_url='/api/v1/users/docs')


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message}
    )


@app.on_event('startup')
async def start_db():
    await init.init_db()

app.include_router(user_router, prefix='/api/v1/users', tags=['Users'])