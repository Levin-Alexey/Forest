"""
Обработчик: Связаться с менеджером
"""
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

# ID закрытой группы для уведомлений
NOTIFICATION_GROUP_ID = -5273547916


class ContactManagerStates(StatesGroup):
    """Состояния для связи с менеджером"""
    waiting_for_question = State()


async def send_question_to_group(bot: Bot, user_id: int, username: str, question: str):
    """
    Отправка вопроса пользователя в закрытую группу
    
    Args:
        bot: Экземпляр бота
        user_id: Telegram ID пользователя
        username: Username пользователя (если есть)
        question: Вопрос пользователя
    """
    try:
        # Формируем сообщение
        user_link = f"@{username}" if username else f"ID: {user_id}"
        message_text = (
            "❓ <b>Новый вопрос от пользователя</b>\n\n"
            f"👤 От: {user_link}\n"
            f"🆔 User ID: <code>{user_id}</code>\n\n"
            f"💬 Вопрос:\n<code>{question}</code>"
        )
        
        # Отправляем сообщение в группу
        await bot.send_message(
            chat_id=NOTIFICATION_GROUP_ID,
            text=message_text,
            parse_mode="HTML"
        )
    except Exception as e:
        # Логируем ошибку, но не прерываем работу бота
        print(f"Ошибка при отправке вопроса в группу: {e}")


@router.callback_query(lambda c: c.data == "contact_manager")
async def contact_manager_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Связаться с менеджером"
    Предлагает пользователю написать свой вопрос
    """
    await callback.answer()
    await state.set_state(ContactManagerStates.waiting_for_question)
    await callback.message.answer(
        "💬 <b>Связь с менеджером</b>\n\n"
        "Напишите ваш вопрос, и мы свяжемся с вами как можно скорее"
    )


@router.message(ContactManagerStates.waiting_for_question)
async def question_received_handler(message: Message, state: FSMContext):
    """
    Обработчик получения вопроса от пользователя
    """
    question = message.text
    user_id = message.from_user.id
    username = message.from_user.username

    # Отправляем вопрос в закрытую группу
    bot = message.bot
    await send_question_to_group(bot, user_id, username, question)

    # Сбрасываем состояние
    await state.clear()

    # Подтверждаем пользователю
    await message.answer(
        "✅ Спасибо за вопрос!\n\n"
        "Наш менеджер свяжется с вами в ближайшее время"
    )
