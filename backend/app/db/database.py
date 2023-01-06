from pymongo import MongoClient
from starlette.config import Config


def get_db_conn(test: bool = False):
    """
    Получить подключение к базе данных
    :param test: Использовать тестовую базу данных?
    :return:
    """
    # test_db_url = "mongodb+srv://npv256:mQHS2EWRM4a-sYs@cluster0.mfvlrbo.mongodb.net/?retryWrites=true&w=majority"
    # db_url = "mongodb+srv://npv256:mQHS2EWRM4a-sYs@cluster0.mfvlrbo.mongodb.net/?retryWrites=true&w=majority"
    # if test:
    #     client = MongoClient(test_db_url, 8000)
    # else:
    #     client = MongoClient(db_url, 8000)
    # db = client["ImagesTest"]
    config = Config(".env")
    db_url = config.get("DATABASE_URL", cast=str) if not test else config.get("TEST_DATABASE_URL", cast=str)
    client = MongoClient(db_url, config.get("DATABASE_PORT", cast=int))
    db_name = config.get("DATABASE_NAME", cast=str) if not test else config.get("TEST_DATABASE_NAME", cast=str)
    db = client[db_name]
    return db

