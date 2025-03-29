import pytest
from decimal import Decimal

from _pytest.python_api import approx
from fastapi.testclient import TestClient

from src.domain.repositories.dto.address import CreateAddressDTO
from src.domain.utils.address import get_address_information
from src.main import app
from src.infrastructure.depends import get_address_service
from src.domain.services.address import AddressService
from src.infrastructure.repositories.address import SQLAlchemyAddressRepository
from tests.infrastructure.db_setup import *


@pytest.fixture
def client():
    async def override_get_address_service():
        repo = SQLAlchemyAddressRepository(test_session_maker)
        service = AddressService(repo)
        return service

    app.dependency_overrides[get_address_service] = override_get_address_service
    return TestClient(app)


@pytest.mark.asyncio
async def test_create_address(client):
    address = 'TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK'
    response = client.post('/v1/address/', json={'address': address})

    assert response.status_code == 200

    data = response.json()
    expected = await get_address_information(CreateAddressDTO(address=address))

    assert data['address'] == expected.address
    assert data['energy'] == expected.energy
    assert data['bandwidth'] == expected.bandwidth
    assert float(data["balance"]) == approx(float(expected.balance), rel=1e-9)
