from src.domain.entities.address import Address
from src.domain.repositories.address import AddressRepository
from src.domain.repositories.dto.address import CreateAddressDTO, GetAddressesDTO
from src.infrastructure.utils.address import get_address_information


class AddressService:
    def __init__(self, repository: AddressRepository):
        self.repository = repository

    async def create(self, create_address: CreateAddressDTO) -> Address:
        addr = await get_address_information(create_address)
        result: Address = await self.repository.create(addr)
        return result

    async def get(self, get_addresses: GetAddressesDTO) -> list[Address]:
        result = await self.repository.get(get_addresses)
        return result
