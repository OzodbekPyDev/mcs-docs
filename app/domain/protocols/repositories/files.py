from typing import Protocol

from app.domain.entities.files import FileEntity
from app.domain.entities.filter_params.files import FilesFilterParams
from app.domain.value_objects.key import KeyVO


class IFilesRepository(Protocol):

    async def get_all(self, filter_params: FilesFilterParams) -> list[FileEntity]:
        raise NotImplementedError

    async def create(self, data: FileEntity) -> None:
        raise NotImplementedError

    async def get_by_key(self, key: KeyVO) -> FileEntity | None:
        raise NotImplementedError

    async def delete_by_key(self, key: KeyVO) -> str:
        raise NotImplementedError

    async def delete_multiple(
        self,
        year: int | None,
        month: int | None,
    ) -> list[str]:
        raise NotImplementedError
