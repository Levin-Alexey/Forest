import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

# Импорт функций для работы с БД
from database import close_db, get_session
from crud import get_or_create_user

# Импорт клавиатур и обработчиков
from keyboards import get_main_menu_keyboard
from handlers.ai_consultant import AIConsultantStates, send_to_webhook
from handlers import (
    ai_consultant_router,
    about_project_router,
    catalog_router,
    video_review_router,
    contact_manager_router,
    links_router,
    # Роутеры резиденций
    residence_a_router,
    residence_b_router,
    residence_c_router,
    residence_d_router,
    residence_e_router,
    residence_f_router,
    residence_g_router,
    residence_h_router,
    residence_i_router,
    residence_k_router,
    # Роутеры резиденции А
    a_presentation_router,
    a_planning_router,
    a_description_router,
    a_photo_gallery_router,
    # Роутеры резиденции Б
    b_presentation_router,
    b_planning_router,
    b_description_router,
    b_photo_gallery_router,
    # Роутеры резиденции В
    c_presentation_router,
    c_planning_router,
    c_description_router,
    c_photo_gallery_router,
    # Роутеры резиденции Г
    d_presentation_router,
    d_planning_router,
    d_description_router,
    d_photo_gallery_router,
    # Роутеры резиденции Д
    e_presentation_router,
    e_planning_router,
    e_description_router,
    e_photo_gallery_router,
    # Роутеры резиденции Е
    f_presentation_router,
    f_planning_router,
    f_description_router,
    f_photo_gallery_router,
    # Роутеры резиденции Ж
    g_presentation_router,
    g_planning_router,
    g_description_router,
    g_photo_gallery_router,
    # Роутеры резиденции З
    h_presentation_router,
    h_planning_router,
    h_description_router,
    h_photo_gallery_router,
    # Роутеры резиденции И
    i_presentation_router,
    i_planning_router,
    i_description_router,
    i_photo_gallery_router,
    # Роутеры резиденции К
    k_presentation_router,
    k_planning_router,
    k_description_router,
    k_photo_gallery_router,
)

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# URL картинки для стартового сообщения
START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"

# Инициализируем бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Создаем fallback роутер для общих сообщений
fallback_router = Router()

# Подключаем роутеры обработчиков (ВАЖНО: ai_consultant_router первым!)
dp.include_router(ai_consultant_router)
dp.include_router(about_project_router)
dp.include_router(catalog_router)
dp.include_router(contact_manager_router)
# Подключаем роутеры резиденций
dp.include_router(residence_a_router)
dp.include_router(residence_b_router)
dp.include_router(residence_c_router)
dp.include_router(residence_d_router)
dp.include_router(residence_e_router)
dp.include_router(residence_f_router)
dp.include_router(residence_g_router)
dp.include_router(residence_h_router)
dp.include_router(residence_i_router)
dp.include_router(residence_k_router)
# Подключаем роутеры резиденции А (обработчики кнопок)
dp.include_router(a_presentation_router)
dp.include_router(a_planning_router)
dp.include_router(a_description_router)
dp.include_router(a_photo_gallery_router)
# Подключаем роутеры резиденции Б (обработчики кнопок)
dp.include_router(b_presentation_router)
dp.include_router(b_planning_router)
dp.include_router(b_description_router)
dp.include_router(b_photo_gallery_router)
# Подключаем роутеры резиденции В (обработчики кнопок)
dp.include_router(c_presentation_router)
dp.include_router(c_planning_router)
dp.include_router(c_description_router)
dp.include_router(c_photo_gallery_router)
# Подключаем роутеры резиденции Г (обработчики кнопок)
dp.include_router(d_presentation_router)
dp.include_router(d_planning_router)
dp.include_router(d_description_router)
dp.include_router(d_photo_gallery_router)
# Подключаем роутеры резиденции Д (обработчики кнопок)
dp.include_router(e_presentation_router)
dp.include_router(e_planning_router)
dp.include_router(e_description_router)
dp.include_router(e_photo_gallery_router)
# Подключаем роутеры резиденции Е (обработчики кнопок)
dp.include_router(f_presentation_router)
dp.include_router(f_planning_router)
dp.include_router(f_description_router)
dp.include_router(f_photo_gallery_router)
# Подключаем роутеры резиденции Ж (обработчики кнопок)
dp.include_router(g_presentation_router)
dp.include_router(g_planning_router)
dp.include_router(g_description_router)
dp.include_router(g_photo_gallery_router)
# Подключаем роутеры резиденции З (обработчики кнопок)
dp.include_router(h_presentation_router)
dp.include_router(h_planning_router)
dp.include_router(h_description_router)
dp.include_router(h_photo_gallery_router)
# Подключаем роутеры резиденции И (обработчики кнопок)
dp.include_router(i_presentation_router)
dp.include_router(i_planning_router)
dp.include_router(i_description_router)
dp.include_router(i_photo_gallery_router)
# Подключаем роутеры резиденции К (обработчики кнопок)
dp.include_router(k_presentation_router)
dp.include_router(k_planning_router)
dp.include_router(k_description_router)
dp.include_router(k_photo_gallery_router)
dp.include_router(video_review_router)
dp.include_router(links_router)
# Подключаем fallback роутер ПОСЛЕДНИМ!
dp.include_router(fallback_router)


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /start
    Сохраняет данные пользователя в БД и отправляет стартовое сообщение с картинкой
    """
    # Сбрасываем состояние FSM (выход из режима AI консультанта)
    await state.clear()

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

    # Отправляем картинку с текстом и inline-клавиатурой
    await message.answer_photo(
        photo=START_IMAGE_URL,
        caption=(
            "<b>Рады приветствовать вас в PISATELI FOREST!</b> 🌲\n\n"
            "Прямо сейчас наш лесной квартал активно оживает: резиденции обретают свой финальный облик, "
            "а интерьеры наполняются авторской мебелью и предметами искусства.\n\n"
            "Я - ваш персональный проводник по проекту, и я готов раскрыть вам каждую деталь будущей жизни в лесу.\n\n"
            "<b>Как со мной общаться?</b>\n\n"
            "Для вашего удобства вся информация разделена на секции в меню ниже.\n\n"
            "⚠️ <b>Важно:</b> Чтобы задать мне вопрос в свободной форме (как обычному человеку), "
            "сначала нажмите кнопку «🤖 AI консультант». После этого я перейду в режим диалога и смогу ответить на любые запросы, например:\n\n"
            "• <b>Из каких материалов построены ваши дома?</b>\n"
            "• <b>Какие инженерные системы применены в резиденциях?</b>\n"
            "• <b>Подбери мне дом со вторым светом</b>"
        ),
        parse_mode="HTML",
        reply_markup=get_main_menu_keyboard()
    )


@dp.message(F.text == "/chat")
async def command_chat_handler(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /chat
    Активирует AI консультанта так же, как кнопка "AI консультант"
    """
    # Переводим пользователя в режим чата с AI
    await state.set_state(AIConsultantStates.chatting)

    await message.answer(
        "🤖 AI консультант активирован!\n\n"
        "Задавайте ваши вопросы, и я постараюсь помочь.\n"
        "Для выхода из режима AI консультанта отправьте /start"
    )


# Обработчик для сообщений в режиме AI консультанта
# ВАЖНО: Должен быть ДО fallback обработчика text_message_handler
@dp.message(AIConsultantStates.chatting, F.text)
async def ai_chat_handler(message: Message) -> None:
    """
    Обработчик сообщений когда пользователь в режиме AI консультанта
    Отправляет сообщение в N8N и возвращает ответ
    """
    user_message = message.text
    user_id = message.from_user.id

    # Показываем статус "печатает...", пока ждем ответ
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

    # Отправляем сообщение в N8N и получаем ответ
    response = await send_to_webhook(user_message, user_id)

    # Отправляем ответ пользователю
    await message.answer(response)




# ВАЖНО: Этот обработчик должен быть ПОСЛЕДНИМ в fallback_router!
# Он ловит только сообщения БЕЗ активного FSM состояния
@fallback_router.message(F.text)
async def text_message_handler(message: Message, state: FSMContext) -> None:
    """
    Обработчик всех текстовых сообщений (fallback)
    Защита от сообщений в чат - направляем пользователя к использованию AI консультанта

    Этот обработчик срабатывает только если:
    - Пользователь НЕ в состоянии AIConsultantStates.chatting
    - Пользователь НЕ заполняет другую форму
    - Нет других более специфичных обработчиков
    """
    # Проверяем, что пользователь не в активном состоянии
    current_state = await state.get_state()
    if current_state is not None:
        # Если есть активное состояние - игнорируем этот обработчик
        # Пусть обработает более специфичный обработчик
        return
    
    await message.answer(
        "💬 Для общения с AI консультантом перейдите в нужный Вам раздел",
        reply_markup=get_main_menu_keyboard()
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