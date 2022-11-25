from beanie import Document


class Message(Document):
    username: str
    is_phone: bool
    message: str

    class Settings:
        name = 'Messages'
    
    class Config:
        schema_extra = {
            'example': {
                'username': 'sampleuser',
                'is_phone': True,
                'message': 'Hello, world!',
            }
        }