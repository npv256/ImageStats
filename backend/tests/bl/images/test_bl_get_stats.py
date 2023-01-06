import pytest
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from app.db.database import get_db_conn
from app.bl.images.get_stats import get_stats
import random
from tests.bl.images.confest import db, images


class TestStatsImages:
    def test_get_stats(self, db, images):
        res = get_stats(db=db)
        assert res is not None
        for key in ["new", "accepted", "deleted", "review"]:
            assert res.get(key) >= 0
        # 5 групп по 5 изображений
        assert sum(res.values()) == 5*5

    def test_get_stats_custom_days(self, db, images):
        res = get_stats(db=db, days=1)
        assert res is not None
        for key in res:
            assert key in ["new", "accepted", "deleted", "review"]
        # 1 группа по 5 изображений
        assert sum(res.values()) == 1 * 5

    # TODO: Проверка передачи некорреткного параметра, рейз исключения
