from typing import Any

from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from routers.speech import router as speech_router


class Settings(BaseModel):
    authjwt_secret_key: str = 'secret' # TODO: Change this later (!!!)


@AuthJWT.load_config
def get_config():
    return Settings()


app = FastAPI(
    openapi_url='/api/v1/speech/openapi.json',
    docs_url='/api/v1/speech/docs'
)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Any | None, exc: AuthJWTException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={'detail': exc.message}
    )


app.include_router(speech_router, prefix='/api/v1/speech', tags=['Speech'])
