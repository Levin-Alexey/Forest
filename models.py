"""
Модели базы данных для Telegram бота
"""
from datetime import datetime
from sqlalchemy import BigInteger, Text, TIMESTAMP, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""
    pass


class User(Base):
    """
    Модель пользователя Telegram бота

    Хранит информацию о пользователях, которые взаимодействуют с ботом
    """
    __tablename__ = "users"

    # telegram_id используем как Primary Key
    # ВАЖНО: Тип BIGINT, так как ID в телеграме длинные числа
    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        comment="Telegram ID пользователя"
    )

    # Имя пользователя (username) из телеграма (@nickname)
    username: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        comment="Username из Telegram (@nickname)"
    )

    # Имя и Фамилия (как подписан в тг)
    first_name: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        comment="Имя пользователя"
    )

    last_name: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        comment="Фамилия пользователя"
    )

    # Телефон (если он поделится контактом или напишет сам)
    phone: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        comment="Номер телефона"
    )

    # Статус клиента (например: 'new', 'consultation', 'deal_closed')
    status: Mapped[str] = mapped_column(
        Text,
        default='new',
        server_default='new',
        comment="Статус клиента"
    )

    # Дата первого обращения (дата старта)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        comment="Дата создания записи"
    )

    # Дата последнего обновления записи (удобно для CRM)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        comment="Дата последнего обновления"
    )

    # Дополнительные данные в формате JSON (на всякий случай)
    extra_data: Mapped[dict] = mapped_column(
        'metadata',  # Имя колонки в БД остается 'metadata'
        JSONB,
        default=dict,
        server_default='{}',
        comment="Дополнительные метаданные в формате JSON"
    )

    # Индекс для быстрого поиска по username
    __table_args__ = (
        Index('idx_users_username', 'username'),
    )

    def __repr__(self) -> str:
        return (
            f"User(telegram_id={self.telegram_id}, "
            f"username={self.username}, "
            f"first_name={self.first_name}, "
            f"status={self.status})"
        )
