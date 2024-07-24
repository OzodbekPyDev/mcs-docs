from uuid import UUID, uuid4

from app.domain.protocols.adapters.id_provider import IIdProvider


class SystemIdProvider(IIdProvider):

    def generate_uuid_v4(self) -> UUID:
        return uuid4()
