"""
Обработчик: Связаться с менеджером
"""
import logging
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from crud import update_user_phone
from database import get_session

logger = logging.getLogger(__name__)
router = Router()

# ID закрытой группы для уведомлений
NOTIFICATION_GROUP_ID = -5273547916


class ContactManagerStates(StatesGroup):
    """Состояния для связи с менеджером"""
    waiting_for_phone = State()


def get_phone_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для передачи номера телефона"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Передать номер телефона", request_contact=True)],
            [KeyboardButton(text="❌ Отменить")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


async def send_contact_to_group(bot: Bot, user_id: int, username: str, phone: str):
    """Отправка контакта пользователя в закрытую группу"""
    try:
        user_link = f"@{username}" if username else f"ID: {user_id}"
        message_text = (
            "☎️ <b>Новый запрос связи с менеджером</b>\n\n"
            f"👤 Пользователь: {user_link}\n"
            f"📱 Телефон: <code>{phone}</code>\n"
            f"🆔 User ID: <code>{user_id}</code>"
        )

        await bot.send_message(
            chat_id=NOTIFICATION_GROUP_ID,
            text=message_text,
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Ошибка при отправке контакта в группу: {e}")


async def start_contact_manager(message_or_callback, state: FSMContext):
    """
    Общая логика для запуска режима связи с менеджером
    """
    try:
        logger.info(f"🔄 Устанавливаю состояние waiting_for_phone")
        await state.set_state(ContactManagerStates.waiting_for_phone)
        logger.info(f"✅ Состояние установлено, отправляю сообщение")
        await message_or_callback.answer(
            "💬 <b>Связь с менеджером</b>\n\n"
            "Живое общение - лучший способ узнать все детали. Наш менеджер уже готов ответить на ваши вопросы по телефону или подобрать удобное время для встречи на объекте.\n\n"
            "Оставьте ваш номер, и мы свяжемся с вами в ближайшее время! 📞",
            reply_markup=get_phone_keyboard()
        )
        logger.info(f"✅ Сообщение отправлено")
    except Exception as e:
        logger.error(f"❌ Ошибка в start_contact_manager: {e}", exc_info=True)


@router.callback_query(lambda c: c.data == "contact_manager")
async def contact_manager_callback_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Связаться с менеджером"
    Предлагает пользователю запросить звонок и передать номер телефона
    """
    logger.info(f"✅ contact_manager callback получен от пользователя {callback.from_user.id}")
    await callback.answer()
    await start_contact_manager(callback.message, state)


@router.message(Command("manager"))
async def contact_manager_command_handler(message: Message, state: FSMContext):
    """
    Обработчик команды /manager
    Предлагает пользователю запросить звонок и передать номер телефона
    """
    await start_contact_manager(message, state)


@router.message(ContactManagerStates.waiting_for_phone, F.text == "❌ Отменить")
async def cancel_contact_manager_handler(message: Message, state: FSMContext):
    """
    Обработчик отмены передачи номера
    """
    await state.clear()
    await message.answer(
        "❌ Передача номера отменена",
        reply_markup=ReplyKeyboardMarkup(keyboard=[[]], resize_keyboard=True)
    )


@router.message(ContactManagerStates.waiting_for_phone, F.contact)
async def contact_received_handler(message: Message, state: FSMContext):
    """Обрабатывает получение контакта с номером телефона"""
    phone = message.contact.phone_number
    user_id = message.from_user.id
    username = message.from_user.username

    async for session in get_session():
        await update_user_phone(session, user_id, phone)

    bot = message.bot
    await send_contact_to_group(bot, user_id, username, phone)

    await state.clear()
    await message.answer(
        f"✅ Спасибо! Номер телефона сохранен: {phone}\n\n"
        "Наш менеджер свяжется с вами в ближайшее время",
        reply_markup=ReplyKeyboardMarkup(keyboard=[[]], resize_keyboard=True)
    )


@router.message(ContactManagerStates.waiting_for_phone, F.text)
async def phone_request_repeat_handler(message: Message):
    """Просим пользователя отправить номер через кнопку"""
    await message.answer(
        "Пожалуйста, нажмите кнопку ниже, чтобы передать номер телефона",
        reply_markup=get_phone_keyboard()
    )
