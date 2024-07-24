from typing import Protocol


class IFileManager(Protocol):

    def secure_name(self, name: str) -> str:
        raise NotImplementedError

    def generate_path(
        self,
        filename: str,
        year: int,
        month: int,
    ) -> str:
        raise NotImplementedError

    def save(
        self,
        path: str,
        content: bytes,
    ) -> None:
        raise NotImplementedError

    def bulk_delete(self, paths: list[str]) -> None:
        raise NotImplementedError

    def delete_by_path(self, path: str) -> None:
        raise NotImplementedError
