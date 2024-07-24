from fastapi import FastAPI

from app.infrastructure.exception_handlers.files import (
    file_not_found_exception_handler,
    save_file_went_wrong_exception_handler,
)
from app.domain.exceptions.files import (
    FileNotFoundException,
    SaveFileWentWrongException,
)


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        FileNotFoundException, handler=file_not_found_exception_handler
    )
    app.add_exception_handler(
        SaveFileWentWrongException, handler=save_file_went_wrong_exception_handler
    )
