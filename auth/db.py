import uuid
from typing import AsyncGenerator

from fastapi import Depends

from fastapi_users.db import SQLAlchemyBaseUserTableUUID,SQLAlchemyUserDatabase
from sqlalchemy import Boolean, Column, String, UUID
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from settings import ConnectorSettings


settings = ConnectorSettings()

DATABASE_URL = (
                f"postgresql+asyncpg://"
                f"{settings.user}:{settings.password.get_secret_value()}"
                f"@{settings.host}:{settings.port}/{settings.database}"
)


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(120), nullable=False)
    surname = Column(String(120), nullable=False)
    about = Column(String(1024), nullable=False)
    email = Column(String(320), index=True, nullable=False)
    hashed_password =  Column(String(1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
