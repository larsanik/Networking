from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from settings import settings as SETTINGS

connection_string = (f"postgresql+asyncpg://{SETTINGS.user}"
                     f":{SETTINGS.password.get_secret_value()}"
                    f"@{SETTINGS.host}:{SETTINGS.port}/{SETTINGS.database}")

engine = create_async_engine(
                            connection_string,
                                future=True,
                                echo=True,
                                connect_args={"ssl": False}) # отключаем ssl
pg_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db_session() -> AsyncSession:
    try:
        session: AsyncSession = pg_session()
        yield session
    finally:
        await session.close()