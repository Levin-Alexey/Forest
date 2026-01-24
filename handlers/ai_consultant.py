"""
Обработчик: AI консультант

AI работает только когда пользователь активировал режим через кнопку "AI консультант".
Кнопка переводит пользователя в FSM состояние AIConsultantStates.chatting.
"""
import os
import logging
import aiohttp
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv

load_dotenv()

router = Router()
logger = logging.getLogger(__name__)

# URL для N8N webhook
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://investretail2026.app.n8n.cloud/webhook/rag_chat")


class AIConsultantStates(StatesGroup):
    """Состояния для работы с AI консультантом"""
    chatting = State()


async def send_to_webhook(message_text: str, user_id: int) -> str:
    """
    Отправляет сообщение на webhook N8N и возвращает ответ

    Args:
        message_text: Текст сообщения пользователя
        user_id: ID пользователя в Telegram

    Returns:
        Ответ от N8N или сообщение об ошибке
    """
    try:
        async with aiohttp.ClientSession() as session:
            # Формируем JSON для отправки в N8N
            payload = {
                "message": message_text,
                "user_id": user_id,
                "chat_id": user_id
            }

            async with session.post(WEBHOOK_URL, json=payload) as response:
                if response.status == 200:
                    # Читаем ответ как текст (N8N настроен на "Respond With: Text")
                    answer_text = await response.text()
                    return answer_text
                else:
                    logger.error(f"Webhook returned status {response.status}")
                    error_text = await response.text()
                    logger.error(f"Server response: {error_text}")
                    return "Извините, произошла ошибка на сервере обработки"
    except Exception as e:
        logger.error(f"Error sending to webhook: {e}")
        return "Извините, не удалось связаться с сервером."


@router.callback_query(lambda c: c.data == "ai_consultant")
async def ai_consultant_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "AI консультант"
    Активирует режим чата с AI
    """
    await callback.answer()

    # Переводим пользователя в режим чата с AI
    await state.set_state(AIConsultantStates.chatting)

    await callback.message.answer(
        "Режим консультации активирован. Я глубоко изучил архитектуру, инженерию и философию PISATELI FOREST, "
        "чтобы дать вам максимально точные ответы.\n\n"
        "Спрашивайте о чем угодно: от технических характеристик резиденций до особенностей ландшафта и инфраструктуры.\n\n"
        "Я на связи 24/7. Но если вы захотите обсудить детали покупки или договориться о визите с человеком - "
        "просто нажмите кнопку «Связаться с менеджером» ниже."
    )


@router.message(AIConsultantStates.chatting, F.text)
async def ai_chat_handler(message: Message, state: FSMContext):
    """
    Обработчик текстовых сообщений в режиме AI консультанта
    """
    # Отправляем сообщение на webhook и получаем ответ
    response = await send_to_webhook(message.text, message.from_user.id)

    # Проверяем, что ответ не пустой (защита от падения бота)
    if response and response.strip():
        await message.answer(response)
    else:
        logger.error(f"Empty response from webhook for user {message.from_user.id}")
        await message.answer("Извините, не удалось получить ответ. Попробуйте позже или переформулируйте вопрос.")
