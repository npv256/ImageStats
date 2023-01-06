import pytest
from fastapi import FastAPI
from async_asgi_testclient import TestClient
from tests.api.images.confest import app, images, client, db

from starlette.status import HTTP_200_OK


class TestImagesRoutes:
    @pytest.mark.asyncio
    async def test_get_stats(self, app: FastAPI, client: TestClient, images, db) -> None:
        res = await client.get(app.url_path_for("images:get_stats"))
        assert res.status_code == HTTP_200_OK
        assert isinstance(res.json(), dict)
        assert len(res.json()) > 0

    # TODO: Проверка исключений при ошибке сервера и клиента
    # TODO: Проверить соответствие результатам БЛ
    # TODO: Проверить фильтрацию и дефолтный отбор в 30 дн
