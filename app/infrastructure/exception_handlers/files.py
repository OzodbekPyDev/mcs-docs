from fastapi import Request
from fastapi.responses import JSONResponse

from app.domain.exceptions.files import (FileNotFoundException,
                                         SaveFileWentWrongException,)


async def file_not_found_exception_handler(
    request: Request, exc: FileNotFoundException
) -> JSONResponse:
    return JSONResponse(status_code=404, content={"message": exc.message})


async def save_file_went_wrong_exception_handler(
    request: Request, exc: SaveFileWentWrongException
) -> JSONResponse:
    return JSONResponse(status_code=500, content={"message": exc.message})
