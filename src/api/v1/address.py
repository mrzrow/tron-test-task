from fastapi import APIRouter, Depends

from src.domain.entities.address import Address
from src.domain.repositories.dto.address import CreateAddressDTO, GetAddressesDTO
from src.domain.services.address import AddressService
from src.infrastructure.depends import get_address_service

router = APIRouter(tags=['Address'], prefix='/address')


@router.post('/', response_model=Address)
async def create(
        create_address: CreateAddressDTO,
        service: AddressService = Depends(get_address_service)
):
    address = await service.create(create_address)
    return address


@router.get('/', response_model=list[Address])
async def get(
        offset: int = 0,
        limit: int = 10,
        service: AddressService = Depends(get_address_service)
):
    get_addresses = GetAddressesDTO(
        offset=offset,
        limit=limit
    )
    addresses = await service.get(get_addresses)
    return addresses
