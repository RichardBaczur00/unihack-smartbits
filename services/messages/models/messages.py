from pydantic import BaseModel


class Message(BaseModel):
    username: str
    is_phone: bool
    message: str