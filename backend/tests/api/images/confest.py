import pytest
from fastapi import FastAPI
from datetime import datetime, timedelta
from async_asgi_testclient import TestClient
from bson.objectid import ObjectId
from app.db.database import get_db_conn
import random


@pytest.fixture(autouse=False)
def db():
    # TODO: Доработать нормальное подключение к тестовой базе, сейчас небезопасно. Добавить миграции.
    data_base = get_db_conn(test=True)
    yield data_base
    data_base["images"].drop()


@pytest.fixture
def app():
    from app.api.server import get_application
    return get_application()


@pytest.fixture
async def client(app: FastAPI) -> TestClient:
    async with TestClient(app) as client:
        yield client


@pytest.fixture
def images(db):
    groups_count = 5
    images_count = 5
    image_list = []

    base_url = "https://example.com/image"
    base_date = datetime.utcnow()
    statuses = ["new", "review", "accepted", "deleted"]
    for group in [f'group{i}' for i in range(groups_count)]:
        for i in range(images_count):
            doc = {
                "_id": ObjectId(),
                "group_name": group,
                "created_at": base_date - timedelta(days=i),
                "changed_at": base_date - timedelta(days=i),
                "url": f"{base_url}-{group}{i + 1}.jpg",
                "status": random.choice(statuses)
            }
            image_list.append(doc)

    coll = db["images"]
    coll.insert_many(image_list)
    return image_list


@pytest.fixture
def image(db):
    base_url = "https://example.com/image"
    base_date = datetime.utcnow()
    doc = {
        "_id": ObjectId(),
        "group_name": 'group1',
        "created_at": base_date,
        "changed_at": base_date,
        "url": f"{base_url}-group1-1.jpg",
        "status": 'new'
    }

    coll = db["images"]
    coll.insert_one(doc)
    return doc
