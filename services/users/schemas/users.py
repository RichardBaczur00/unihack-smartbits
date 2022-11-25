from beanie import Document

from pydantic import EmailStr

class User(Document):
    username: str
    password: str
    email: EmailStr

    class Settings:
        name = 'Users'

    class Config:
        schema_extra = {
            'example': {
                'username': 'sampleuser',
                'password': 'samplepass',
                'email': 'sample@email.tst',
            }
        }