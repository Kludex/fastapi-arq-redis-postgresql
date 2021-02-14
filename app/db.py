from typing import Generator

from humps import depascalize
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_async_engine(settings.POSTGRES_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@as_declarative()
class Base:
    __name__: str

    @declared_attr()
    def __tablename__(cls) -> str:
        return depascalize(cls.__name__)


async def get_session() -> Generator:
    with SessionLocal() as session:
        yield session
