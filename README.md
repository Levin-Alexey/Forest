# Forest Bot - Telegram Bot с PostgreSQL

Telegram бот с интеграцией PostgreSQL для хранения информации о пользователях и взаимодействия с n8n webhook.

## Структура проекта

```
forest_bot/
├── main.py           # Основной файл бота
├── models.py         # SQLAlchemy модели (таблица users)
├── database.py       # Конфигурация подключения к БД
├── crud.py           # CRUD операции для работы с пользователями
├── requirements.txt  # Зависимости проекта
├── .env             # Переменные окружения (не в репозитории)
└── .env.example     # Пример файла с переменными окружения
```

## Установка

### 1. Клонируйте репозиторий и перейдите в директорию проекта

```bash
cd forest_bot
```

### 2. Создайте виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux/Mac
# или
venv\Scripts\activate     # Для Windows
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Настройте переменные окружения

Скопируйте файл `.env.example` в `.env` и заполните необходимые данные:

```bash
cp .env.example .env
```

Отредактируйте `.env`:

```env
BOT_TOKEN=your_telegram_bot_token_here
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/forest_bot
WEBHOOK_URL=https://investretail2026.app.n8n.cloud/webhook/rag_chat
```

### 5. Подготовьте базу данных PostgreSQL

**Если таблица users уже существует в базе данных** - можно пропустить этот шаг.

**Если нужно создать таблицу:**

В файле `main.py` раскомментируйте строки:

```python
# await init_db()
# logger.info("База данных инициализирована")
```

Это создаст таблицу `users` при первом запуске бота.

## Модель данных

### Таблица `users`

Схема таблицы users соответствует вашей PostgreSQL схеме:

| Поле | Тип | Описание |
|------|-----|----------|
| telegram_id | BIGINT (PK) | ID пользователя в Telegram |
| username | TEXT | Username из Telegram (@nickname) |
| first_name | TEXT | Имя пользователя |
| last_name | TEXT | Фамилия пользователя |
| phone | TEXT | Номер телефона |
| status | TEXT | Статус клиента (по умолчанию 'new') |
| created_at | TIMESTAMP WITH TIME ZONE | Дата создания записи |
| updated_at | TIMESTAMP WITH TIME ZONE | Дата последнего обновления |
| metadata | JSONB | Дополнительные данные в формате JSON |

## Запуск бота

```bash
python main.py
```

## Использование

### CRUD операции

В файле `crud.py` реализованы следующие функции:

- `get_user(session, telegram_id)` - получить пользователя по ID
- `create_user(session, telegram_id, ...)` - создать нового пользователя
- `update_user(session, telegram_id, **kwargs)` - обновить данные пользователя
- `get_or_create_user(session, telegram_id, ...)` - получить или создать пользователя
- `update_user_status(session, telegram_id, status)` - обновить статус пользователя
- `update_user_metadata(session, telegram_id, extra_data)` - обновить метаданные

### Пример использования в коде

```python
from database import get_session
from crud import get_or_create_user, update_user_status

# Создание или получение пользователя
async for session in get_session():
    user, created = await get_or_create_user(
        session,
        telegram_id=123456789,
        username="john_doe",
        first_name="John",
        last_name="Doe"
    )
    print(f"User: {user}, Created: {created}")

# Обновление статуса пользователя
async for session in get_session():
    user = await update_user_status(
        session,
        telegram_id=123456789,
        status="consultation"
    )
```

## Особенности реализации

1. **Асинхронная работа с БД** - используется `asyncpg` для PostgreSQL
2. **Автоматическое обновление пользователей** - при каждом сообщении данные пользователя обновляются
3. **INSERT ... ON CONFLICT** - используется PostgreSQL-специфичная конструкция для эффективного upsert
4. **Индекс по username** - для быстрого поиска пользователей
5. **JSONB метаданные** - для хранения дополнительных данных в гибком формате

## Примечания

- В продакшене рекомендуется использовать Alembic для управления миграциями базы данных
- При использовании `init_db()` будьте осторожны - эта функция создаст все таблицы заново
- Поле `metadata` в модели называется `extra_data` во избежание конфликта с атрибутом SQLAlchemy
- Логирование SQL запросов можно включить, установив `echo=True` в `database.py`

## Лицензия

MIT
