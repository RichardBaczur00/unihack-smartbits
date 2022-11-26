from pydantic import BaseModel


class Message(BaseModel):
    glove_address: str
    is_phone: bool
    message: str


class MessageRetrieval(BaseModel):
    glove_address: str


class MessageDeletion(MessageRetrieval):
    pass