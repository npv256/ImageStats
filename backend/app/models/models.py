from pydantic import BaseModel
from datetime import datetime
from typing import List

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


class ImageUpdate(ImageBase):
    """
    Модель изображения при обновлении
    """
    status: StatusType


class ImageGroupBase(BaseModel):
    """
    Модель группы изображений
    """
    _id: str
    name: str
    images: List[ImageBase]
    count: int
