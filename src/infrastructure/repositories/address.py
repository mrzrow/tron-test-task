from sqlalchemy import select

from src.domain.entities.address import Address
from src.domain.repositories.address import AddressRepository
from src.domain.repositories.dto.address import GetAddressesDTO
from src.infrastructure.database.session_maker import SessionMaker
from src.infrastructure.database.models.address import AddressModel


class SQLAlchemyAddressRepository(AddressRepository):
    def __init__(self, session_maker: SessionMaker):
        self.session_maker = session_maker

    async def create(self, create_address: Address) -> Address:
        async with self.session_maker.get_session() as session:
            address_dump = create_address.model_dump()
            address = AddressModel(**address_dump)
            session.add(address)
            await session.commit()
            await session.refresh(address)
            return Address(
                id=address.id,
                address=address.address,
                balance=address.balance,
                bandwidth=address.bandwidth,
                energy=address.energy,
                timestamp=address.timestamp
            )

    async def get(self, get_addresses: GetAddressesDTO) -> list[Address]:
        async with self.session_maker.get_session() as session:
            offset, limit = get_addresses.offset, get_addresses.limit
            stmt = select(AddressModel).order_by(AddressModel.timestamp.desc()).offset(offset).limit(limit)
            result = await session.execute(stmt)
            addresses = result.scalars()
            return list(addresses)
