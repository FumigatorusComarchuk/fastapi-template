from typing import AsyncIterable

from dishka import Provider, Scope, provide, AnyOf
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.application import interfaces
from src.config import Config
from src.infrastructure.database.session_maker import new_session_maker


class DatabaseSessionProvider(Provider):
    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[
        AnyOf[
            AsyncSession,
            interfaces.DBSession,
        ]
    ]:
        async with session_maker() as session:
            yield session
