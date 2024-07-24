from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.files import FileEntity
from app.domain.entities.filter_params.files import FilesFilterParams
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.value_objects.key import KeyVO
from app.infrastructure.db.models.sqlalchemy_orm.files import File


class SqlalchemyFilesRepository(IFilesRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self, filter_params: FilesFilterParams) -> list[FileEntity]:
        query = select(File)

        if filter_params.year:
            query = query.where(File.year == filter_params.year)
        if filter_params.month:
            query = query.where(File.month == filter_params.month)

        result = await self.session.execute(query)
        items = result.scalars().all()

        return [item.to_entity() for item in items]

    async def create(self, data: FileEntity) -> None:
        query = insert(File).values(
            id=data.id.value,
            key=data.key.value,
            name=data.name,
            year=data.year,
            month=data.month,
            path=data.path,
            expiration_date=data.expiration_date,
        )

        await self.session.execute(query)

    async def get_by_key(self, key: KeyVO) -> FileEntity | None:
        query = select(File).where(File.key == key.value)

        result = await self.session.execute(query)
        item = result.scalar_one_or_none()

        return item.to_entity() if item else None

    async def delete_by_key(self, key: KeyVO) -> str:

        query = delete(File).where(File.key == key.value).returning(File.path)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def delete_multiple(self, year: int = None, month: int = None) -> list[str]:
        query = delete(File).returning(File.path)

        if year:
            query = query.where(File.year == year)

        if month:
            query = query.where(File.month == month)

        result = await self.session.execute(query)

        paths = result.scalars().all()
        return [path for path in paths]
