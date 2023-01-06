import pytest
from fastapi import FastAPI
from async_asgi_testclient import TestClient
from tests.api.images.confest import app, images, client, db

from starlette.status import (
    HTTP_200_OK
)


class TestImagesRoutes:
    @pytest.mark.asyncio
    async def test_update_status(self, app: FastAPI, client: TestClient, images, db) -> None:
        new_status = 'review'
        image = images.pop()
        assert image is not None
        res = await client.put(app.url_path_for("images:update_status", id_=str(image.get('_id')), status=new_status))
        assert res.status_code == HTTP_200_OK

    # TODO: Проверка исключений при ошибке сервера и клиента
    # TODO: Проверить соответствие результатам БЛ
    # TODO: Проверка неккорентых параметров
    # TODO: Проверка обновления несуществующего изображения
