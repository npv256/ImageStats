from datetime import datetime, timedelta
from bson.objectid import ObjectId
import random
from app.db.database import get_db_conn


def generate_data(num_docs=20):
    docs = []
    base_url = "https://example.com/image"
    base_date = datetime.utcnow()
    statuses = ["new", "review", "accepted", "deleted"]

    for group in [f'group{i}' for i in range(10)]:
        for i in range(num_docs):
            doc = {
                "_id": ObjectId(),
                "group_name": group,
                "created_at": base_date + timedelta(hours=i),
                "changed_at": base_date + timedelta(hours=i),
                "url": f"{base_url}-{group}{i + 1}.jpg",
                "status": random.choice(statuses)
            }
            docs.append(doc)

    db = get_db_conn()
    coll = db["images"]
    coll.insert_many(docs)
