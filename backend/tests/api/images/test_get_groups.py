import pytest
from fastapi import FastAPI
from async_asgi_testclient import TestClient

from starlette.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
)


@pytest.fixture
def app() -> FastAPI:
    from app.api.server import get_application
    return get_application()


@pytest.fixture
async def client(app: FastAPI) -> TestClient:
    async with TestClient(app) as client:
        yield client


class TestImagesRoutes:
    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: TestClient) -> None:
        res = await client.get(app.url_path_for("images:get_groups", status=None))
        assert res.status_code != HTTP_404_NOT_FOUND
