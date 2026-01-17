"""
Обработчик: Каталог резиденций
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .catalog_handlers.keyboards import get_catalog_keyboard

router = Router()

# URL картинки для главного меню
START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"


@router.callback_query(lambda c: c.data == "catalog")
async def catalog_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Каталог резиденций"
    """
    await callback.answer()
    await callback.message.answer(
        "🏢 <b>Каталог резиденций</b>\n\n"
        "Тут будет описание\n\n"
        "Выберите интересующую вас резиденцию:",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Назад в меню"
    Возвращает пользователя в главное меню как при /start
    """
    await callback.answer()

    # Сбрасываем состояние FSM
    await state.clear()

    # Импортируем здесь чтобы избежать циклических импортов
    from keyboards import get_main_menu_keyboard

    # Отправляем картинку с главным меню
    await callback.message.answer_photo(
        photo=START_IMAGE_URL,
        caption="Я виртуальный помощник. Выберете пункт меню",
        reply_markup=get_main_menu_keyboard()
    )


