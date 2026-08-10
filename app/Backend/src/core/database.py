from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .config import settings


engine = create_async_engine(
    url=settings.database_url,
    echo=True, #Parameter indicates that SQL emitted by connections will be logged to standard out. When prod - turn off.
)

async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=True,
    expire_on_commit=False
)

class Base(DeclarativeBase): pass

async def async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session_maker() as session:
        yield session