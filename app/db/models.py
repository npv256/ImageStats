from pydantic import BaseModel
from datetime import datetime


class ImageModel(BaseModel):
    _id: str
    created_at: datetime
    changed_at: datetime
    group_name: str
    url: str
    status: str
