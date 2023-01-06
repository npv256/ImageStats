import pytest
from fastapi import FastAPI
from async_asgi_testclient import TestClient
from tests.api.images.confest import app, images, client, db
from starlette.status import HTTP_200_OK


class TestImagesRoutes:
    @pytest.mark.asyncio
    async def test_get_all_groups(self, app: FastAPI, client: TestClient, images, db) -> None:
        res = await client.get(app.url_path_for("images:get_groups"))
        assert res.status_code == HTTP_200_OK
        assert isinstance(res.json(), list)
        assert len(res.json()) > 0
        # TODO: Проверить наличие всех полей и соответствие с методом БЛ

    # TODO: Проверить корректный возврат при отсутствии данных
    # TODO: Проверить фильтрацию по статусу
    # TODO: Проверка исключений при ошибке сервера и клиента, неправильные параметры и тд
    # TODO: Проверить плагинацию
