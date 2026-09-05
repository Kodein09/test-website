from typing import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .config import settings


async_engine = async_sessionmaker(
    url=settings.database_url,
    echo=True, #Parameter indicates that SQL emitted by connections will be logged to standard out. When prod - turn off.
    connect_args={"check_same_thread": False}
)

SessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=True,
    expire_on_commit=False
)

Base = declarative_base()

async def async_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def init_db():
    Base.metadata.create_all(bind=async_engine)