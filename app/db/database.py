from pymongo import MongoClient
from starlette.config import Config

config = Config(".env")


def get_db_conn():
    client = MongoClient(config.get("DATABASE_URL", cast=str), config.get("DATABASE_PORT", cast=int))
    db = client[config.get("DATABASE_NAME", cast=str)]
    return db
