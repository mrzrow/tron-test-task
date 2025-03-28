import pytest
import pytest_asyncio

from datetime import datetime
from decimal import Decimal

from src.domain.entities.address import Address
from src.infrastructure.database.models.base import Base
from src.infrastructure.database.session_maker import SessionMaker
from src.infrastructure.repositories.address import SQLAlchemyAddressRepository
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


@pytest.mark.asyncio
async def test_create_address():
    repo = SQLAlchemyAddressRepository(test_session_maker)

    address = Address(
        address='fake_address',
        balance=Decimal(100),
        bandwidth=100,
        energy=100,
        timestamp=datetime.utcnow()
    )
    result_address = await repo.create(address)

    assert address.address == result_address.address
    assert address.balance == result_address.balance
    assert address.bandwidth == result_address.bandwidth
    assert address.energy == result_address.energy
    assert address.timestamp == result_address.timestamp
