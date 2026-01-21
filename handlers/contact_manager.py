"""
Обработчик: Связаться с менеджером
"""
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

# ID закрытой группы для уведомлений
NOTIFICATION_GROUP_ID = -5273547916


class ContactManagerStates(StatesGroup):
    """Состояния для связи с менеджером"""
    waiting_for_question = State()


def get_cancel_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура с кнопкой отмены"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="❌ Отменить")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


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


async def start_contact_manager(message_or_callback, state: FSMContext):
    """
    Общая логика для запуска режима связи с менеджером
    """
    await state.set_state(ContactManagerStates.waiting_for_question)
    await message_or_callback.answer(
        "💬 <b>Связь с менеджером</b>\n\n"
        "Напишите ваш вопрос, и мы свяжемся с вами как можно скорее",
        reply_markup=get_cancel_keyboard()
    )


@router.callback_query(lambda c: c.data == "contact_manager")
async def contact_manager_callback_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Связаться с менеджером"
    Предлагает пользователю написать свой вопрос
    """
    await callback.answer()
    await start_contact_manager(callback.message, state)


@router.message(Command("manager"))
async def contact_manager_command_handler(message: Message, state: FSMContext):
    """
    Обработчик команды /manager
    Предлагает пользователю написать свой вопрос
    """
    await start_contact_manager(message, state)


@router.message(ContactManagerStates.waiting_for_question, F.text == "❌ Отменить")
async def cancel_contact_manager_handler(message: Message, state: FSMContext):
    """
    Обработчик отмены отправки вопроса
    """
    await state.clear()
    await message.answer(
        "❌ Отправка вопроса отменена",
        reply_markup=ReplyKeyboardMarkup(keyboard=[[]], resize_keyboard=True)
    )


@router.message(ContactManagerStates.waiting_for_question, F.text)
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
        "Наш менеджер свяжется с вами в ближайшее время",
        reply_markup=ReplyKeyboardMarkup(keyboard=[[]], resize_keyboard=True)
    )
