"""
Конфигурация и подключение к базе данных
"""
import os
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

from models import Base

# Загружаем переменные окружения
load_dotenv()

# Получаем URL для подключения к PostgreSQL из переменных окружения
# Формат: postgresql+asyncpg://user:password@host:port/database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://user:password@localhost:5432/forest_bot"
)

# Создаем асинхронный движок
# echo=True включает логирование SQL запросов (для отладки)
# poolclass=NullPool отключает пул соединений (полезно для serverless)
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Установите True для отладки SQL запросов
    poolclass=NullPool,
)

# Создаем фабрику сессий
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Генератор асинхронных сессий для работы с БД

    Использование:
        async with get_session() as session:
            # Работа с базой данных
            pass
    """
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db() -> None:
    """
    Инициализация базы данных
    Создает все таблицы, определенные в моделях

    ВНИМАНИЕ: Используйте только для разработки!
    В продакшене лучше использовать Alembic для миграций
    """
    from sqlalchemy.ext.asyncio import AsyncConnection

    async with engine.begin() as conn:  # type: AsyncConnection
        # Удаляем все таблицы (осторожно!)
        # await conn.run_sync(Base.metadata.drop_all)

        # Создаем все таблицы
        await conn.run_sync(Base.metadata.create_all)


async def close_db() -> None:
    """
    Закрытие соединения с базой данных
    Вызывать при завершении работы приложения
    """
    await engine.dispose()
