import uuid
import time

from gtts import gTTS


async def read_message(
    message: str,
    language_code: str = 'ro',
    tld: str = 'com',
    slow: bool = False
):
    return gTTS(message, tld=tld, lang=language_code, slow=slow)


async def save_audio_to_tmp(
    message: str,
    language_code: str = 'ro',
    tld: str = 'com',
    slow: bool = False
):
    id = uuid.uuid4()
    ttl = time.time() + 5 * 60
    data = await read_message(message, language_code, tld, slow)

    data.save(f'./tmp/{id}-{int(ttl)}.mp3')

    return f'{id}-{int(ttl)}'
