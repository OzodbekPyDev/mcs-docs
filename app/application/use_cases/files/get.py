from uuid import UUID

from app.application.dto.files import FileResponse, GetListFilesRequest
from app.application.protocols.interactor import Interactor
from app.domain.entities.filter_params.files import FilesFilterParams
from app.domain.exceptions.files import FileNotFoundException
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.protocols.repositories.uow import IUnitOfWork
from app.domain.value_objects.key import KeyVO


class GetListFiles(Interactor[GetListFilesRequest, list[FileResponse]]):
    def __init__(
        self,
        uow: IUnitOfWork,
        files_repository: IFilesRepository,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository

    async def __call__(self, request: GetListFilesRequest) -> list[FileResponse]:
        files = await self.files_repository.get_all(
            filter_params=FilesFilterParams(year=request.year, month=request.month)
        )
        return [FileResponse.from_entity(file) for file in files]


class GetFileByKey(Interactor[UUID, FileResponse]):

    def __init__(
        self,
        uow: IUnitOfWork,
        files_repository: IFilesRepository,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository

    async def __call__(self, request: UUID) -> FileResponse:
        file_entity = await self.files_repository.get_by_key(key=KeyVO(value=request))
        if not file_entity:
            raise FileNotFoundException("File not found with that key!")

        return FileResponse.from_entity(file_entity)
