import pytest
from app.bl.images.get_stats import get_stats
from app.models.models import StatusType
from tests.bl.images.confest import db, images


class TestStatsImages:
    def test_get_stats(self, db, images):
        res = get_stats(db=db)
        assert res is not None
        for key in [e.value for e in StatusType]:
            assert res.get(key) >= 0
        # 5 групп по 5 изображений
        assert sum(res.values()) == 5*5

    def test_get_stats_custom_days(self, db, images):
        res = get_stats(db=db, days=1)
        assert res is not None
        for key in res:
            assert key in [e.value for e in StatusType]
        # 1 группа по 5 изображений
        assert sum(res.values()) == 1 * 5

    # TODO: Проверка передачи некорреткного параметра, рейз исключения
