from src.domain.services.address import AddressService
from src.infrastructure.database.session_maker import session_maker
from src.infrastructure.repositories.address import SQLAlchemyAddressRepository


async def get_address_service() -> AddressService:
    repo = SQLAlchemyAddressRepository(session_maker)
    service = AddressService(repo)
    return service
