from app.application.dto.files import FileResponse, UpdateFileRequest
from app.application.protocols.interactor import Interactor
from app.domain.exceptions.files import FileNotFoundException
from app.domain.protocols.adapters.file_manager import IFileManager
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.protocols.repositories.uow import IUnitOfWork
from app.domain.value_objects.key import KeyVO


class UpdateFileContentByKey(Interactor[UpdateFileRequest, FileResponse]):

    def __init__(
        self,
        uow: IUnitOfWork,
        files_repository: IFilesRepository,
        file_manager: IFileManager,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository
        self.file_manager = file_manager

    async def __call__(self, request: UpdateFileRequest) -> FileResponse:
        file_entity = await self.files_repository.get_by_key(
            key=KeyVO(value=request.key)
        )
        if not file_entity:
            raise FileNotFoundException("File not found with that key!")

        self.file_manager.save(path=file_entity.path, content=request.content)
        return FileResponse.from_entity(file_entity)
