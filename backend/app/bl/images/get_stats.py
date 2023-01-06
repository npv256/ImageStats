from typing import Dict, Optional
from datetime import datetime, timedelta
from app.db.database import get_db_conn


def get_stats(db=None, days: Optional[int] = None) -> Dict:
    """
    Получить статистику по изображениям
    :param db: БД
    :param days: Кол-во дней, за которую необходимо получить статистику
    :return Словарь в формате: {"status": int, ex: "new": 5}
    """
    if days is None:
        days = 30
    cutoff_date = datetime.utcnow() - timedelta(days=days)

    pipeline = [
        {
            "$match": {
                "changed_at": {
                    "$gte": cutoff_date
                }
            }
        },
        {
            "$group": {
                "_id": "$status",
                "count": {"$sum": 1}
            }
        }
    ]
    if db is None:
        db = get_db_conn()
    images = db["images"]
    result = list(images.aggregate(pipeline))
    return {doc["_id"]: doc["count"] for doc in result}

