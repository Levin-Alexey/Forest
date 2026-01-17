# Миграции с Alembic

Alembic уже установлен в зависимостях проекта. Вот как его использовать:

## Инициализация Alembic (если еще не сделано)

```bash
alembic init alembic
```

## Настройка Alembic

1. Отредактируйте файл `alembic.ini` и закомментируйте строку:
```ini
# sqlalchemy.url = driver://user:pass@localhost/dbname
```

2. Отредактируйте файл `alembic/env.py`:

```python
# В начале файла добавьте импорты
import os
from dotenv import load_dotenv
from models import Base

load_dotenv()

# Найдите строку target_metadata и замените на:
target_metadata = Base.metadata

# Найдите функцию get_url() или создайте её:
def get_url():
    return os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/forest_bot")

# В функции run_migrations_offline() замените:
url = get_url()

# В функции run_migrations_online() замените:
configuration = config.get_section(config.config_ini_section)
configuration["sqlalchemy.url"] = get_url()
```

## Создание миграции

```bash
# Автоматическое создание миграции на основе моделей
alembic revision --autogenerate -m "Initial migration"

# Применение миграции
alembic upgrade head

# Откат миграции
alembic downgrade -1
```

## Полезные команды

```bash
# Показать текущую версию БД
alembic current

# Показать историю миграций
alembic history

# Откатиться к определённой версии
alembic downgrade <revision_id>

# Применить все миграции
alembic upgrade head
```

## Примечание

Если таблица `users` уже существует в PostgreSQL, и вы хотите начать использовать Alembic:

1. Создайте первую миграцию:
```bash
alembic revision --autogenerate -m "Initial migration"
```

2. Отредактируйте созданный файл миграции и удалите команду создания таблицы `users`

3. Пометьте текущее состояние БД как "migrated":
```bash
alembic stamp head
```

Теперь все последующие изменения в моделях можно будет применять через миграции.
