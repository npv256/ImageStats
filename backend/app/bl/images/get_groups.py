from typing import List, Optional
from app.db.database import get_db_conn
from app.models.models import ImageGroupBase, ImageBase


def get_groups(db=None, page: Optional[int] = None, page_size: Optional[int] = None, status: Optional[str] = None) \
        -> List[ImageGroupBase]:
    """
    Получить группы изображений
    :param db: БД
    :param page: Страница с результатами
    :param page_size Кол-во групп на странице
    :param status: Статус изображения
    """
    if page is None:
        page = 1
    if page_size is None:
        page_size = 20
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
                        "group_name": "$group_name",
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

    if status is not None and status != '':
        pipeline.insert(1, {"$match": {"status": status}})
    if db is None:
        db = get_db_conn()
    images = db["images"]
    db_res = list(images.aggregate(pipeline))
    groups = []
    for group in db_res:
        model_images = []
        for image in group.get('images'):
            model_image = ImageBase(**image)
            model_images.append(model_image)
        group['images'] = model_images
        groups.append(ImageGroupBase(**group))

    return groups
