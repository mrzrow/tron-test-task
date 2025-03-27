from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.core.settings import settings


class SessionMaker:
    def __init__(self, path: str, echo: bool = False):
        self.engine = create_async_engine(
            url=path,
            echo=echo
        )
        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        async with self.session_maker() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()


session_maker = SessionMaker(
    path=settings.db.path,
    echo=settings.db.echo
)
