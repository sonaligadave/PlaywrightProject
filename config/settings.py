import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    BASE_URL = os.getenv("BASE_URL")
    BASE_URL_API = os.getenv("BASE_URL_API")