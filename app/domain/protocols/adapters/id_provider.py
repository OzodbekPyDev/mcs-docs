from typing import Protocol
from uuid import UUID


class IIdProvider(Protocol):

    def generate_uuid_v4(self) -> UUID:
        pass
