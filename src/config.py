import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp-relay.brevo.com')
    SMTP_PORT = os.getenv('SMTP_PORT', 587)
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', '7e75dd001@smtp-brevo.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '5Yv0E3fFqbgK4UjL')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', 'username@gmail.com')
    