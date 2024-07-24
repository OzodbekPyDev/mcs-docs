from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class KeyVO:
    value: UUID
