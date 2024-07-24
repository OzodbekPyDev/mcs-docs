from datetime import timedelta

from app.application.dto.files import CreateFileRequest, FileResponse
from app.application.protocols.interactor import Interactor
from app.domain.entities.files import FileEntity
from app.domain.protocols.adapters.datetime_provider import DateTimeProvider
from app.domain.protocols.adapters.file_manager import IFileManager
from app.domain.protocols.adapters.id_provider import IIdProvider
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.protocols.repositories.uow import IUnitOfWork
from app.domain.value_objects.id import IdVO
from app.domain.value_objects.key import KeyVO


class CreateFile(Interactor[CreateFileRequest, FileResponse]):

    def __init__(
        self,
        uow: IUnitOfWork,
        files_repository: IFilesRepository,
        id_provider: IIdProvider,
        file_manager: IFileManager,
        datetime_provider: DateTimeProvider,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository
        self.id_provider = id_provider
        self.file_manager = file_manager
        self.datetime_provider = datetime_provider

    async def __call__(self, request: CreateFileRequest) -> FileResponse:
        secured_filename = self.file_manager.secure_name(request.name)

        current_datetime = self.datetime_provider.get_current_time()
        generated_file_path = self.file_manager.generate_path(
            filename=secured_filename,
            year=current_datetime.year,
            month=current_datetime.month,
        )

        file_entity = FileEntity(
            id=IdVO(value=self.id_provider.generate_uuid_v4()),
            key=KeyVO(value=request.key),
            name=secured_filename,
            year=current_datetime.year,
            month=current_datetime.month,
            path=generated_file_path,
            expiration_date=current_datetime + timedelta(days=365 * 8),
        )

        await self.files_repository.create(file_entity)

        self.file_manager.save(
            path=file_entity.path,
            content=request.content,
        )
        await self.uow.commit()
        return FileResponse.from_entity(file_entity)
