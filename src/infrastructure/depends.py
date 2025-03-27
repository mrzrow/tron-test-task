from src.domain.services.address import AddressService
from src.infrastructure.repositories.address import SQLAlchemyAddressRepository


async def get_address_service() -> AddressService:
    repo = SQLAlchemyAddressRepository()
    service = AddressService(repo)
    return service
