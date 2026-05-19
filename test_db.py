# Для теста подключения к базе данных.
import asyncio
import asyncpg

async def test():
    try:
        # Пробуем подключиться к Docker напрямую через asyncpg
        conn = await asyncpg.connect('postgresql://postgres:postgres@127.0.0.1:5433/postgres')
        print("🎉 Успех! Чистый asyncpg смог подключиться к Docker!")
        await conn.close()
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")

asyncio.run(test())