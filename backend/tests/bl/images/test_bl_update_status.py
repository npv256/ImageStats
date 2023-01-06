import pytest
from bson.objectid import ObjectId
from app.bl.images.update_status import update_status
from tests.bl.images.confest import db, image


class TestStatsImages:

    def test_update_status(self, db, image):
        new_status = 'review'
        _id = image.get('_id')
        old_status = db["images"].find_one({"_id": ObjectId(_id)}).get('status')
        assert old_status != new_status
        res = update_status(_id, new_status, db=db)
        assert res == _id
        assert new_status == db["images"].find_one({"_id": ObjectId(_id)}).get('status')

    def test_update_status_image_not_found(self, db, image):
        new_status = 'review'
        _id = '5f8c9d92937e932e7c0dcbbe'
        res = update_status(_id, new_status, db=db)
        assert res is None

    def test_update_status_incorrect_status(self, db, image):
        new_status = 'randoon_status'
        _id = image.get('_id')
        old_status = db["images"].find_one({"_id": ObjectId(_id)}).get('status')
        assert old_status != new_status
        try:
            res = update_status(_id, new_status, db=db)
            assert False
        except Exception:
            pass

    # TODO: Ошибка в бд, корректный рейз исключения
