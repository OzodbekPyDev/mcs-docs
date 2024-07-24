from dishka import Provider, Scope, provide
from dishka.integrations.fastapi import FromDishka

from app.application.use_cases.files.create import CreateFile
from app.application.use_cases.files.delete import (DeleteFileByKey,
                                                    DeleteMultipleFiles,)
from app.application.use_cases.files.get import GetFileByKey, GetListFiles
from app.application.use_cases.files.update import UpdateFileContentByKey
from app.domain.protocols.adapters.datetime_provider import DateTimeProvider
from app.domain.protocols.adapters.file_manager import IFileManager
from app.domain.protocols.adapters.id_provider import IIdProvider
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.protocols.repositories.uow import IUnitOfWork


class FilesInteractorProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_get_list(
        self,
        uow: FromDishka[IUnitOfWork],
        files_repository: FromDishka[IFilesRepository],
    ) -> GetListFiles:
        return GetListFiles(uow=uow, files_repository=files_repository)

    @provide(scope=Scope.REQUEST)
    def provide_create(
        self,
        uow: FromDishka[IUnitOfWork],
        files_repository: FromDishka[IFilesRepository],
        id_provider: FromDishka[IIdProvider],
        datetime_provider: FromDishka[DateTimeProvider],
        file_manager: FromDishka[IFileManager],
    ) -> CreateFile:
        return CreateFile(
            uow=uow,
            files_repository=files_repository,
            id_provider=id_provider,
            file_manager=file_manager,
            datetime_provider=datetime_provider,
        )

    @provide(scope=Scope.REQUEST)
    def provide_get_by_key(
        self,
        uow: FromDishka[IUnitOfWork],
        files_repository: FromDishka[IFilesRepository],
    ) -> GetFileByKey:
        return GetFileByKey(uow=uow, files_repository=files_repository)

    @provide(scope=Scope.REQUEST)
    def provide_update_file_content_by_key(
        self,
        uow: FromDishka[IUnitOfWork],
        files_repository: FromDishka[IFilesRepository],
        file_manager: FromDishka[IFileManager],
    ) -> UpdateFileContentByKey:
        return UpdateFileContentByKey(
            uow=uow, files_repository=files_repository, file_manager=file_manager
        )

    @provide(scope=Scope.REQUEST)
    def provide_delete_file_by_key(
        self,
        uow: FromDishka[IUnitOfWork],
        files_repository: FromDishka[IFilesRepository],
        file_manager: FromDishka[IFileManager],
    ) -> DeleteFileByKey:
        return DeleteFileByKey(
            uow=uow, files_repository=files_repository, file_manager=file_manager
        )

    @provide(scope=Scope.REQUEST)
    def provide_delete_multiple_files(
        self,
        uow: FromDishka[IUnitOfWork],
        files_repository: FromDishka[IFilesRepository],
        file_manager: FromDishka[IFileManager],
    ) -> DeleteMultipleFiles:
        return DeleteMultipleFiles(
            uow=uow, files_repository=files_repository, file_manager=file_manager
        )
