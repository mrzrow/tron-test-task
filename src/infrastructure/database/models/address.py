from decimal import Decimal
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DATETIME

from src.infrastructure.database.models.base import Base


class AddressModel(Base):
    address: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[Decimal] = mapped_column()
    bandwidth: Mapped[int] = mapped_column()
    energy: Mapped[int] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
