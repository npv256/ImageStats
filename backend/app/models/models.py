from pydantic import BaseModel, validator
from datetime import datetime

from enum import Enum


class StatusType(str, Enum):
    """
    Возможные статусы изображения
    """
    new = "new"
    review = "review"
    accepted = "accepted"
    deleted = "deleted"


class ImageBase(BaseModel):
    """
    Базовая модель изображения
    """
    _id: str
    created_at: datetime
    changed_at: datetime
    group_name: str
    url: str
    status: StatusType = StatusType.new

    @validator("created_at", "changed_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()


class ImageUpdate(BaseModel):
    """
    Модель изображения при обновлении
    """
    status: StatusType

