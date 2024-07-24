from dataclasses import dataclass
from datetime import datetime

from app.domain.entities.base import BaseEntity
from app.domain.value_objects.key import KeyVO


@dataclass
class FileEntity(BaseEntity):
    key: KeyVO
    name: str
    year: int
    month: int
    path: str
    expiration_date: datetime
