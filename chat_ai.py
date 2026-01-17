import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import aiohttp
from dotenv import load_dotenv

# Импорт функций для работы с БД
from database import init_db, close_db, get_session
from crud import get_or_create_user

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# !!! ИСПРАВЛЕНИЕ 1: Убрали лишние пробелы в ссылке !!!
WEBHOOK_URL = "https://investretail2026.app.n8n.cloud/webhook/rag_chat"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def send_to_webhook(message_text: str, user_id: int) -> str:
    """
    Отправляет сообщение на webhook и возвращает ответ
    """
    try:
        async with aiohttp.ClientSession() as session:
            # Формируем JSON, который отправляем В n8n (это правильно)
            payload = {
                "message": message_text,
                "user_id": user_id,
                "chat_id": user_id  # Лучше добавить chat_id явно, n8n его любит
            }

            async with session.post(WEBHOOK_URL, json=payload) as response:
                if response.status == 200:
                    # !!! ИСПРАВЛЕНИЕ 2: Читаем ответ как ТЕКСТ, а не JSON !!!
                    # Так как в n8n мы поставили "Respond With: Text"
                    answer_text = await response.text()
                    return answer_text
                else:
                    logger.error(f"Webhook returned status {response.status}")
                    # Можно прочитать текст ошибки для отладки
                    error_text = await response.text()
                    logger.error(f"Server response: {error_text}")
                    return "Извините, произошла ошибка на сервере обработки"
    except Exception as e:
        logger.error(f"Error sending to webhook: {e}")
        return "Извините, не удалось связаться с сервером."


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Сохраняем пользователя в базу данных
    async for session in get_session():
        user, created = await get_or_create_user(
            session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

        if created:
            logger.info(f"Новый пользователь создан: {user.telegram_id} (@{user.username})")
        else:
            logger.info(f"Пользователь обновлен: {user.telegram_id} (@{user.username})")

    await message.answer("Добрый день! Готов Вам помочь!")


@dp.message(F.text)
async def message_handler(message: Message) -> None:
    user_message = message.text
    user_id = message.from_user.id

    # Сохраняем/обновляем пользователя в базе данных
    async for session in get_session():
        await get_or_create_user(
            session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

    # Показываем статус "печатает...", пока ждем ответ
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")

    response = await send_to_webhook(user_message, user_id)

    await message.answer(response)


async def main():
    logger.info("Бот запускается...")

    # Инициализация базы данных (создание таблиц, если их нет)
    # Раскомментируйте если база данных еще не создана
    # await init_db()
    # logger.info("База данных инициализирована")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await close_db()
        logger.info("Соединение с базой данных закрыто")


if __name__ == "__main__":
    asyncio.run(main())