from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from app.domain.entities.files import FileEntity
from app.domain.value_objects.id import IdVO
from app.domain.value_objects.key import KeyVO
from app.infrastructure.db.models.sqlalchemy_orm.base import Base


class File(Base):
    __tablename__ = "files"

    key: Mapped[UUID] = mapped_column(index=True, unique=True)
    name: Mapped[str]
    year: Mapped[int]
    month: Mapped[int]
    path: Mapped[str]
    expiration_date: Mapped[datetime]

    def to_entity(self) -> FileEntity:
        return FileEntity(
            id=IdVO(value=self.id),
            key=KeyVO(value=self.key),
            name=self.name,
            year=self.year,
            month=self.month,
            path=self.path,
            expiration_date=self.expiration_date,
        )
