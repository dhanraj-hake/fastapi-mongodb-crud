
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mongodb_uri: str = ""
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

client = MongoClient(settings.mongodb_uri, server_api=ServerApi('1'))
db = client.fastapi_crud
item_collection = db.items
clockin_collection = db.user_clockin