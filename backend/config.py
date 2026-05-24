import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flutterwave
    FLW_CLIENT_ID = os.getenv("FLW_CLIENT_ID")
    FLW_SECRET_KEY = os.getenv("FLW_SECRET_KEY")
    FLW_ENCRYPTION_KEY = os.getenv("FLW_ENCRYPTION_KEY")

    # Africa's Talking
    AT_API_KEY = os.getenv("AT_API_KEY")
    AT_USERNAME = os.getenv("AT_USERNAME")

    # Flask
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    DEBUG = os.getenv("DEBUG", "False") == "True"