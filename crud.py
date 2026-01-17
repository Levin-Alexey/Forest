"""
CRUD операции для работы с пользователями
"""
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from models import User


async def get_user(session: AsyncSession, telegram_id: int) -> Optional[User]:
    """
    Получить пользователя по telegram_id

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя

    Returns:
        User или None, если пользователь не найден
    """
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()


async def create_user(
    session: AsyncSession,
    telegram_id: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    status: str = "new",
    extra_data: Optional[dict] = None,
) -> User:
    """
    Создать нового пользователя

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя
        username: Username из Telegram
        first_name: Имя пользователя
        last_name: Фамилия пользователя
        phone: Номер телефона
        status: Статус клиента
        extra_data: Дополнительные метаданные

    Returns:
        Созданный объект User
    """
    user = User(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        status=status,
        extra_data=extra_data or {},
    )
    session.add(user)
    await session.flush()
    await session.refresh(user)
    return user


async def update_user(
    session: AsyncSession,
    telegram_id: int,
    **kwargs
) -> Optional[User]:
    """
    Обновить данные пользователя

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя
        **kwargs: Поля для обновления

    Returns:
        Обновленный объект User или None
    """
    # Добавляем автоматическое обновление updated_at (с timezone)
    kwargs['updated_at'] = datetime.now(timezone.utc)

    await session.execute(
        update(User)
        .where(User.telegram_id == telegram_id)
        .values(**kwargs)
    )
    await session.flush()

    # Возвращаем обновленного пользователя
    return await get_user(session, telegram_id)


async def get_or_create_user(
    session: AsyncSession,
    telegram_id: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
) -> tuple[User, bool]:
    """
    Получить существующего пользователя или создать нового

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя
        username: Username из Telegram
        first_name: Имя пользователя
        last_name: Фамилия пользователя
        phone: Номер телефона

    Returns:
        Кортеж (User, created), где created=True если пользователь был создан
    """
    now_utc = datetime.now(timezone.utc)

    # Используем PostgreSQL-специфичную конструкцию INSERT ... ON CONFLICT
    stmt = insert(User).values(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
    ).on_conflict_do_update(
        index_elements=['telegram_id'],
        set_={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'updated_at': now_utc,
        }
    ).returning(User)

    result = await session.execute(stmt)
    user = result.scalar_one()
    await session.flush()
    await session.refresh(user)

    # Проверяем, был ли пользователь только что создан
    # Оба datetime теперь имеют timezone info
    created = (now_utc - user.created_at).total_seconds() < 1

    return user, created


async def update_user_status(
    session: AsyncSession,
    telegram_id: int,
    status: str
) -> Optional[User]:
    """
    Обновить статус пользователя

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя
        status: Новый статус

    Returns:
        Обновленный объект User или None
    """
    return await update_user(session, telegram_id, status=status)


async def update_user_metadata(
    session: AsyncSession,
    telegram_id: int,
    extra_data: dict
) -> Optional[User]:
    """
    Обновить метаданные пользователя

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя
        extra_data: Новые метаданные (будут объединены с существующими)

    Returns:
        Обновленный объект User или None
    """
    user = await get_user(session, telegram_id)
    if user:
        # Объединяем существующие метаданные с новыми
        new_metadata = {**user.extra_data, **extra_data}
        return await update_user(session, telegram_id, extra_data=new_metadata)
    return None


async def update_user_phone(
    session: AsyncSession,
    telegram_id: int,
    phone: str
) -> Optional[User]:
    """
    Обновить номер телефона пользователя

    Args:
        session: Асинхронная сессия БД
        telegram_id: Telegram ID пользователя
        phone: Номер телефона

    Returns:
        Обновленный объект User или None
    """
    return await update_user(session, telegram_id, phone=phone)

