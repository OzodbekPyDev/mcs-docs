from dishka import Provider, Scope, provide
from dishka.integrations.fastapi import FromDishka
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.protocols.repositories.uow import IUnitOfWork
from app.infrastructure.repositories.sqlalchemy_orm.files import \
    SqlalchemyFilesRepository
from app.infrastructure.repositories.sqlalchemy_orm.uow import \
    SqlalchemyUnitOfWork


class RepositoriesProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_uow_repository(self, session: FromDishka[AsyncSession]) -> IUnitOfWork:
        return SqlalchemyUnitOfWork(session)

    @provide(scope=Scope.REQUEST)
    def provide_files_repository(
        self, session: FromDishka[AsyncSession]
    ) -> IFilesRepository:
        return SqlalchemyFilesRepository(session)
