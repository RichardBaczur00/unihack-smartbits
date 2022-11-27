import os

from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from routers.files import router as files_router


# TODO: Consider protecting certain files with this
class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv('JWT_SECRET', 'secret')


@AuthJWT.load_config
def get_config():
    return Settings()


app = FastAPI(
    openapi_url='/api/v1/files/openapi.json',
    docs_url='/api/v1/files/docs'
)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={'detail': exc.message}
    )


app.include_router(files_router, prefix='/api/v1/files', tags=['Files'])