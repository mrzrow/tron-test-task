from pydantic import BaseModel


class CreateAddressDTO(BaseModel):
    address: str


class GetAddressesDTO(BaseModel):
    offset: int
    limit: int
