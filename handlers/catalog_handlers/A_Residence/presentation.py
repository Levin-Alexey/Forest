"""
Обработчик: Получить презентацию (Резиденция А)
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from crud import update_user_phone, get_user
from database import get_session

router = Router()

# Презентация URL
PRESENTATION_URL = "https://s3.twcstorage.ru/d0419efa-bbfb6254-e439-47a2-b99f-612b4490d542/present/1.pdf"


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


@router.callback_query(lambda c: c.data == "a_presentation")
async def a_presentation_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Получить презентацию" для резиденции А
    Проверяет наличие номера телефона в БД
    """
    await callback.answer()
    user_id = callback.from_user.id

    # Получаем пользователя из БД
    async for session in get_session():
        user = await get_user(session, user_id)

        # Если номер телефона уже есть - отправляем ссылку
        if user and user.phone:
            await callback.message.answer(
                f"✅ Номер телефона найден: {user.phone}\n\n"
                f"📄 Вот ссылка на презентацию резиденции:\n"
                f"{PRESENTATION_URL}"
            )
            return

    # Номера телефона нет - запрашиваем контакт
    await state.set_state(PresentationStates.waiting_for_contact)
    await callback.message.answer(
        "📊 <b>Презентация Резиденции А</b>\n\n"
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

    # Сохраняем номер телефона в БД
    async for session in get_session():
        await update_user_phone(session, user_id, phone)

    # Сбрасываем состояние
    await state.clear()

    # Отправляем ссылку на презентацию
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
