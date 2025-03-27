from fastapi import APIRouter

from .v1.address import router as address_router
from ..core.settings import settings

router_v1 = APIRouter(prefix=settings.api_path)
router_v1.include_router(address_router)
