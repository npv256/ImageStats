from pymongo import MongoClient
from starlette.config import Config

import logging

logger = logging.getLogger(__name__)


def get_db_conn(test: bool = False):
    """
    Получить подключение к базе данных
    :param test: Использовать тестовую базу данных?
    :return:
    """
    try:
        config = Config(".env")
        db_url = config.get("DATABASE_URL", cast=str) if not test else config.get("TEST_DATABASE_URL", cast=str)
        client = MongoClient(db_url, config.get("DATABASE_PORT", cast=int))
        db_name = config.get("DATABASE_NAME", cast=str) if not test else config.get("TEST_DATABASE_NAME", cast=str)
        db = client[db_name]
        return db
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")

