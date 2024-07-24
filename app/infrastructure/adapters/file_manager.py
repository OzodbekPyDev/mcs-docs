import os

from uuid6 import uuid6

from app.domain.exceptions.files import SaveFileWentWrongException
from app.domain.protocols.adapters.file_manager import IFileManager


class SystemFileManager(IFileManager):

    def secure_name(self, name: str) -> str:
        return f"{uuid6()}.{name}"

    def generate_path(
        self,
        filename: str,
        year: int,
        month: int,
    ) -> str:
        # Create the directory path
        directory = f"app/media/{year}/{month}"

        # Make directories if they don't exist
        os.makedirs(directory, exist_ok=True)

        # Create the full path for the file
        return f"{directory}/{filename}"

    def save(self, path: str, content: bytes) -> None:
        try:

            # Save the content to the file
            with open(path, "wb") as f:
                f.write(content)
        except Exception as e:
            raise SaveFileWentWrongException(str(e))

    def bulk_delete(self, paths: list[str]) -> None:
        for path in paths:
            self.delete_by_path(path)

    def delete_by_path(self, path: str) -> None:
        try:
            os.remove(path)
            month_dir = os.path.dirname(path)
            if not os.listdir(month_dir):  # Проверяет, пустая ли директория
                os.rmdir(month_dir)  # Удаляет директорию (по месяцам)

            year_dir = os.path.dirname(month_dir)
            if not os.listdir(year_dir):
                os.rmdir(year_dir)  # Удаляет директорию (по годам)

        except Exception as e:
            raise SaveFileWentWrongException(str(e))
