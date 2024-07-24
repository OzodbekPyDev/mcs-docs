from typing import Annotated
from uuid import UUID

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Depends, File, Form, UploadFile, status
from fastapi.responses import FileResponse as FastAPIFileResponse

from app.application.dto.files import (CreateFileRequest,
                                       DeleteMultipleFilesRequest,
                                       FileResponse, GetListFilesRequest,
                                       UpdateFileRequest,)
from app.application.use_cases.files.create import CreateFile
from app.application.use_cases.files.delete import (DeleteFileByKey,
                                                    DeleteMultipleFiles,)
from app.application.use_cases.files.get import GetFileByKey, GetListFiles
from app.application.use_cases.files.update import UpdateFileContentByKey


router = APIRouter(prefix="/files", tags=["files"], route_class=DishkaRoute)


@router.get("/")
async def get_files(
    request: Annotated[GetListFilesRequest, Depends()],
    get_list_files_interactor: FromDishka[GetListFiles],
) -> list[FileResponse]:
    return await get_list_files_interactor(request)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_file(
    key: Annotated[UUID, Form()],
    file: Annotated[UploadFile, File()],
    create_file_interactor: FromDishka[CreateFile],
) -> FileResponse:
    request = CreateFileRequest(key=key, name=file.filename, content=await file.read())
    return await create_file_interactor(request)


@router.get("/{key}")
async def get_file_by_key(
    key: UUID, get_file_by_key_interactor: FromDishka[GetFileByKey]
) -> FastAPIFileResponse:
    file_item = await get_file_by_key_interactor(key)
    return FastAPIFileResponse(path=file_item.path, filename=file_item.name)


@router.put("/{key}")
async def update_file_content_by_key(
    key: UUID,
    file: Annotated[UploadFile, File()],
    update_file_content_by_key_interactor: FromDishka[UpdateFileContentByKey],
) -> FileResponse:
    request = UpdateFileRequest(key=key, content=await file.read())
    return await update_file_content_by_key_interactor(request)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_multiple_files(
    request: DeleteMultipleFilesRequest,
    delete_all_files_interactor: FromDishka[DeleteMultipleFiles],
) -> None:
    return await delete_all_files_interactor(request)


@router.delete("/{key}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file_by_key(
    key: UUID, delete_file_by_key_interactor: FromDishka[DeleteFileByKey]
) -> None:
    return await delete_file_by_key_interactor(key)
