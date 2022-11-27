from pydantic import BaseModel


class FileQuery(BaseModel):
    name: str