import os
import time

from typing import Any

from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from routers.speech import router as speech_router


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv('JWT_SECRET', 'secret')


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

@app.on_event('startup')
@repeat_every(seconds=10*60) # every ten minutes
def clear_tmp_directory():
    all_files = map(
        lambda p: (int(p.split('-')[-1].split('.')[0]), p),
        os.listdir('./tmp/')
    )

    old_files = filter(
        lambda p: time.time() >= p[0],
        all_files
    )

    for _, file in old_files:
        os.remove(file)


app.include_router(speech_router, prefix='/api/v1/speech', tags=['Speech'])
