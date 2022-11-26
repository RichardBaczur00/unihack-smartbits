from gtts import gTTS


async def read_message(
    message: str,
    language_code: str = 'ro',
    tld: str = 'com',
    slow: bool = False
):
    return gTTS(message, tld=tld, lang=language_code, slow=slow)