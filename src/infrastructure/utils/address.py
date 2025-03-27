import traceback
from tronpy import AsyncTron
from tronpy.keys import to_hex_address
from tronpy.providers import AsyncHTTPProvider

from src.core.settings import settings
from src.domain.entities.address import Address
from src.domain.repositories.dto.address import CreateAddressDTO


async def get_address_information(create_address: CreateAddressDTO) -> Address:
    provider = AsyncHTTPProvider("https://api.trongrid.io", api_key=settings.tron_api_key)
    async with AsyncTron(provider=provider) as client:
        try:
            address = create_address.address
            hex_address = to_hex_address(address)
            balance = await client.get_account_balance(hex_address)
            resources = await client.get_account_resource(hex_address)
            bandwidth = resources.get('free_net_usage', 0)
            energy = resources.get('EnergyUsage', 0)
        except Exception as e:
            raise ValueError(f'Error fetching data: {e}')

        return Address(
            address=address,
            balance=balance,
            bandwidth=bandwidth,
            energy=energy
        )
