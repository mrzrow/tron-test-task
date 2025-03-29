import pytest

from datetime import datetime
from decimal import Decimal

from src.domain.entities.address import Address
from src.infrastructure.repositories.address import SQLAlchemyAddressRepository

from tests.infrastructure.db_setup import *


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
