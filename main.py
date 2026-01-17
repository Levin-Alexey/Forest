import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

# Импорт функций для работы с БД
from database import close_db, get_session
from crud import get_or_create_user

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# URL картинки для стартового сообщения
START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start
    Сохраняет данные пользователя в БД и отправляет стартовое сообщение с картинкой
    """
    user_id = message.from_user.id

    # Сохраняем/обновляем данные пользователя в базе данных
    async for session in get_session():
        user, created = await get_or_create_user(
            session,
            telegram_id=user_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

        if created:
            logger.info(
                f"✅ Новый пользователь создан: "
                f"ID={user.telegram_id}, "
                f"username={user.username}, "
                f"name={user.first_name} {user.last_name}"
            )
        else:
            logger.info(
                f"🔄 Пользователь обновлен: "
                f"ID={user.telegram_id}, "
                f"username={user.username}"
            )

    # Отправляем картинку с текстом
    await message.answer_photo(
        photo=START_IMAGE_URL,
        caption="Я виртуальный помощник. Выберете пункт меню"
    )


async def main():
    logger.info("🚀 Бот запускается...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await close_db()
        logger.info("🛑 Бот остановлен, соединение с БД закрыто")


if __name__ == "__main__":
    asyncio.run(main())