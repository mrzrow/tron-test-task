from abc import ABC, abstractmethod

from src.domain.entities.address import Address
from src.domain.repositories.dto.address import GetAddressesDTO


class AddressRepository(ABC):
    @abstractmethod
    async def create(self, create_address: Address) -> Address:
        raise NotImplementedError

    @abstractmethod
    async def get(self, get_addresses: GetAddressesDTO) -> list[Address]:
        raise NotImplementedError
