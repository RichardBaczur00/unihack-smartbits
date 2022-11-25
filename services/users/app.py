from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from db import init

from models import users as users_models

from services import users as user_services


class Settings(BaseModel):
    authjwt_secret_key: str = 'secret' # TODO: Change this later (!!!)


@AuthJWT.load_config
def get_config():
    return Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app = FastAPI()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message}
    )


@app.on_event('startup')
async def start_db():
    await init.init_db()


@app.post('/signup')
async def register(user: users_models.UserRegister, Authorize: AuthJWT = Depends()):
    return await user_services.register_services(user, Authorize)


@app.post('/signin')
async def login(user: users_models.UserLogin, Authorize: AuthJWT = Depends()):
    return await user_services.login_services(user, Authorize)


@app.get('/')
def index():
    return {'Message': 'Hello world!'}