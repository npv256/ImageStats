from typing import Optional
from app.db.database import get_db_conn
from datetime import datetime
from bson.objectid import ObjectId


def update_status(id_: str, status: str, db=None) -> Optional[str]:
    """
    Обновить статус изображения
    :param db: БД
    :param id_: Идентификатор изображения
    :param status: Новый статус изображения
    :return Идентификатор обновленного изображения
    """
    if not id_ or not status:
        # TODO: Отедельное исключение
        raise Exception('Not correct params')
    try:
        obj_id = ObjectId(id_)
    except Exception:
        raise Exception("Id is not correct")

    if status not in ['new', 'accepted', 'review', 'deleted']:
        # TODO: Отедельное исключение
        raise Exception('Not correct params')

    if db is None:
        db = get_db_conn()
    images = db["images"]
    result = images.update_one(
        {"_id": obj_id},
        {
            "$set": {
                "status": status,
                "changed_at": datetime.utcnow()
            }
        }
    )

    return id_ if result.modified_count > 0 else None

