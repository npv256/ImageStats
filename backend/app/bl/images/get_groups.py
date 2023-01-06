from typing import List, Dict, Optional
from app.db.database import get_db_conn


def get_groups(db=None, page: int = 1, page_size: int = 10, status: Optional[str] = None) -> List[Dict]:
    """
    Получить группы изображений
    :param db: БД
    :param page: Страница с результатами
    :param page_size Кол-во групп на странице
    :param status: Статус изображения
    """
    if status and status not in ['new', 'review', 'accepted', 'deleted']:
        # TODO: Создать отдельный тип Exception
        raise Exception('Incorrect status')

    pipeline = [
        {
            "$sort": {"created_at": -1}
        },
        {
            "$group": {
                "_id": "$group_name",
                "name": {"$first": "$group_name"},
                "images": {
                    "$push": {
                        "id": "$_id",
                        "created_at": "$created_at",
                        "changed_at": "$changed_at",
                        "url": "$url",
                        "status": "$status"
                    }
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$skip": (page - 1) * page_size
        },
        {
            "$limit": page_size
        }
    ]

    if status is not None:
        pipeline.insert(1, {"$match": {"status": status}})
    if db is None:
        db = get_db_conn()
    images = db["images"]
    result = list(images.aggregate(pipeline))
    return result
