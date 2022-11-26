from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from db import init

from routers.messages import router as messages_router


class Settings(BaseModel):
    authjwt_secret_key: str = 'secret' # TODO: Change this later (!!!)


@AuthJWT.load_config
def get_config():
    return Settings()

app = FastAPI(
    openapi_url='/api/v1/messages/openapi.json', 
    docs_url='/api/v1/messages/docs'
)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={'detail': exc.message}
    )


@app.on_event('startup')
async def start_db():
    await init.init_db()


app.include_router(messages_router, prefix='/api/v1/messages', tags=['Messages'])
