"""
Обработчик: Получить презентацию (Резиденция Е)
"""
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from crud import update_user_phone, get_user
from database import get_session

router = Router()

# Презентация URL
PRESENTATION_URL = "https://s3.twcstorage.ru/d0419efa-bbfb6254-e439-47a2-b99f-612b4490d542/present/6.pdf"

# ID закрытой группы для уведомлений
NOTIFICATION_GROUP_ID = -5273547916


class PresentationStates(StatesGroup):
    """Состояния для получения презентации"""
    waiting_for_contact = State()


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


async def send_notification_to_group(bot: Bot, user_id: int, username: str, phone: str):
    """
    Отправка уведомления в закрытую группу о получении нового контакта
    
    Args:
        bot: Экземпляр бота
        user_id: Telegram ID пользователя
        username: Username пользователя (если есть)
        phone: Номер телефона пользователя
    """
    try:
        # Формируем сообщение
        user_link = f"@{username}" if username else f"ID: {user_id}"
        message_text = (
            "🆕 <b>Новая заявка на презентацию (Резиденция Е)</b>\n\n"
            f"👤 Пользователь: {user_link}\n"
            f"📱 Телефон: <code>{phone}</code>\n"
            f"🆔 User ID: <code>{user_id}</code>"
        )
        
        # Отправляем сообщение в группу
        await bot.send_message(
            chat_id=NOTIFICATION_GROUP_ID,
            text=message_text,
            parse_mode="HTML"
        )
    except Exception as e:
        # Логируем ошибку, но не прерываем работу бота
        print(f"Ошибка при отправке уведомления в группу: {e}")


@router.callback_query(lambda c: c.data == "f_presentation")
async def f_presentation_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Получить презентацию" для резиденции Е
    Проверяет наличие номера телефона в БД
    """
    await callback.answer()
    user_id = callback.from_user.id

    # Получаем пользователя из БД
    async for session in get_session():
        user = await get_user(session, user_id)

        # Если номер телефона уже есть - отправляем ссылку
        if user and user.phone:
            await callback.message.answer_document(
                PRESENTATION_URL,
                caption="PDF файл презентации"
            )
            await callback.message.answer(
                f"✅ Номер телефона найден: {user.phone}\n\n"
                f"📄 Вот ссылка на презентацию резиденции:\n"
                f"{PRESENTATION_URL}"
            )
            return

    # Номера телефона нет - запрашиваем контакт
    await state.set_state(PresentationStates.waiting_for_contact)
    await callback.message.answer(
        "📊 <b>Презентация Резиденции Е</b>\n\n"
        "Для получения презентации нажмите кнопку поделиться контактом",
        reply_markup=get_phone_keyboard()
    )


@router.message(PresentationStates.waiting_for_contact, F.contact)
async def contact_received_handler(message: Message, state: FSMContext):
    """
    Обработчик получения контакта с номером телефона
    """
    phone = message.contact.phone_number
    user_id = message.from_user.id
    username = message.from_user.username

    # Сохраняем номер телефона в БД
    async for session in get_session():
        await update_user_phone(session, user_id, phone)

    # Отправляем уведомление в закрытую группу
    bot = message.bot
    await send_notification_to_group(bot, user_id, username, phone)

    # Сбрасываем состояние
    await state.clear()

    # Отправляем ссылку на презентацию
    await message.answer_document(
        PRESENTATION_URL,
        caption="PDF файл презентации"
    )
    await message.answer(
        f"✅ Спасибо! Номер телефона сохранен: {phone}\n\n"
        f"📄 Вот ссылка на презентацию резиденции:\n"
        f"{PRESENTATION_URL}"
    )


@router.message(PresentationStates.waiting_for_contact, F.text == "❌ Отменить")
async def cancel_presentation_handler(message: Message, state: FSMContext):
    """
    Обработчик отмены получения презентации
    """
    await state.clear()
    await message.answer(
        "❌ Получение презентации отменено"
    )
