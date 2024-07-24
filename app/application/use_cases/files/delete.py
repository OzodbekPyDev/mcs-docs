from uuid import UUID

from app.application.dto.files import DeleteMultipleFilesRequest
from app.application.protocols.interactor import Interactor
from app.domain.protocols.adapters.file_manager import IFileManager
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.protocols.repositories.uow import IUnitOfWork
from app.domain.value_objects.key import KeyVO


class DeleteMultipleFiles(Interactor[DeleteMultipleFilesRequest, None]):

    def __init__(
        self,
        uow: IUnitOfWork,
        files_repository: IFilesRepository,
        file_manager: IFileManager,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository
        self.file_manager = file_manager

    async def __call__(self, request: DeleteMultipleFilesRequest) -> None:
        file_paths = await self.files_repository.delete_multiple(
            year=request.year, month=request.month
        )
        await self.uow.commit()
        self.file_manager.bulk_delete(file_paths)
        return


class DeleteFileByKey(Interactor[UUID, None]):

    def __init__(
        self,
        uow: IUnitOfWork,
        files_repository: IFilesRepository,
        file_manager: IFileManager,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository
        self.file_manager = file_manager

    async def __call__(self, request: UUID) -> None:
        file_path = await self.files_repository.delete_by_key(key=KeyVO(value=request))
        await self.uow.commit()
        self.file_manager.delete_by_path(file_path)
        return
