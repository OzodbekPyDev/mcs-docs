from dishka import Provider, Scope, provide

from app.domain.protocols.adapters.datetime_provider import DateTimeProvider
from app.domain.protocols.adapters.file_manager import IFileManager
from app.domain.protocols.adapters.id_provider import IIdProvider
from app.infrastructure.adapters.datetime_provider import (
    SystemDateTimeProvider, Timezone,)
from app.infrastructure.adapters.file_manager import SystemFileManager
from app.infrastructure.adapters.id_provider import SystemIdProvider


class AdaptersProvider(Provider):

    @provide(scope=Scope.APP)
    def provide_id_adapter(self) -> IIdProvider:
        return SystemIdProvider()

    @provide(scope=Scope.APP)
    def provide_date_time_provider(self) -> DateTimeProvider:
        return SystemDateTimeProvider(Timezone.UTC)

    @provide(scope=Scope.APP)
    def provide_file_manager(self) -> IFileManager:
        return SystemFileManager()
