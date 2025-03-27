from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api import router_v1
from src.infrastructure.database.models.base import Base
from src.infrastructure.database.session_maker import session_maker


@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with session_maker.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield
    finally:
        await session_maker.engine.dispose()


app = FastAPI(title='URL-Shortener', lifespan=lifespan)
app.include_router(router=router_v1)

if __name__ == '__main__':
    uvicorn.run(app)
