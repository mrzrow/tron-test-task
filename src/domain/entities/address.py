from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class Address(BaseModel):
    id: int | None = None
    address: str
    balance: Decimal
    bandwidth: int
    energy: int
    timestamp: datetime = datetime.utcnow()
