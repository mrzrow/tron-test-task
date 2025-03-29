import pytest_asyncio

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.session_maker import SessionMaker

from tests.settings import test_settings

test_session_maker = SessionMaker(
    path=test_settings.db.path,
    echo=test_settings.db.echo
)


@pytest_asyncio.fixture(scope='function', autouse=True)
async def lifespan():
    async with test_session_maker.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield
    finally:
        await test_session_maker.engine.dispose()
