from dataclasses import dataclass


@dataclass
class FilesFilterParams:
    year: int | None
    month: int | None
