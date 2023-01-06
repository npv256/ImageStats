import pytest
from app.bl.images.get_groups import get_groups
from tests.bl.images.confest import db, images
from app.models.models import StatusType


class TestGroupsImages:
    def test_get_groups(self, db, images):
        res = get_groups(db=db)
        assert res is not None
        assert len(res) == 5
        for group in res:
            assert group.count == 5
            assert group.images is not None

    def test_get_groups_by_status(self, db, images):
        statuses = [e.value for e in StatusType]
        for status in statuses:
            res = get_groups(db=db, status=status)
            assert res is not None
            for group in res:
                group_images = group.images
                for image in group_images:
                    assert image.status == status

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
            for image in group.images:
                if not prev_image_created_at:
                    prev_image_created_at = image.created_at
                    continue
                assert image.created_at < prev_image_created_at
                prev_image_created_at = image.created_at

    # TODO: Проверить что метод отработает, если в бд будет слишком много данных
    # TODO: Нет данных, метод вернет пустой список
    # TODO: Проверить, что рейзятся конкретные исключения на каждую проблему: БД, некорректный статус и тд
