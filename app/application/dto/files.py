from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.entities.files import FileEntity


@dataclass
class CreateFileRequest:
    key: UUID
    name: str
    content: bytes


@dataclass
class UpdateFileRequest:
    key: UUID
    content: bytes


@dataclass
class DeleteMultipleFilesRequest:
    year: int | None
    month: int | None


@dataclass
class FileResponse:
    id: UUID
    key: UUID
    name: str
    year: int
    month: int
    path: str
    expiration_date: datetime

    @classmethod
    def from_entity(cls, entity: FileEntity) -> "FileResponse":
        return cls(
            id=entity.id.value,
            key=entity.key.value,
            name=entity.name,
            year=entity.year,
            month=entity.month,
            path=entity.path,
            expiration_date=entity.expiration_date,
        )


@dataclass
class GetListFilesRequest:
    year: int | None = None
    month: int | None = None
