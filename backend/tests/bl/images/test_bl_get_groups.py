import pytest
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from app.db.database import get_db_conn
from app.bl.images.get_groups import get_groups
import random
from tests.bl.images.confest import db, images


class TestGroupsImages:
    def test_get_groups(self, db, images):
        res = get_groups(db=db)
        assert res is not None
        assert len(res) == 5
        for group in res:
            assert group.get('count') == 5
            assert group.get('images') is not None

    def test_get_groups_by_status(self, db, images):
        statuses = ['new', 'accepted', 'review', 'deleted']
        for status in statuses:
            res = get_groups(db=db, status=status)
            assert res is not None
            for group in res:
                group_images = group.get('images')
                for image in group_images:
                    assert image.get('status') == status

    def test_get_groups_by_invalid_status(self, db, images):
        try:
            res = get_groups(db=db, status='incorrect_status_123')
            assert False
        except Exception:
            pass

    def test_get_groups_order_images(self, db):
        res = get_groups(db=db)
        for group in res:
            prev_image_created_at = None
            for image in group.get('images'):
                if not prev_image_created_at:
                    prev_image_created_at = image.get('created_at')
                    continue
                assert image.get('created_at') < prev_image_created_at
                prev_image_created_at = image.get('created_at')

    # TODO: Проверить что метод отработает, если в бд будет слишком много данных
    # TODO: Нет данных, метод вернет пустой список
    # TODO: Проверить, что рейзятся конкретные исключения на каждую проблему: БД, некорректный статус и тд
