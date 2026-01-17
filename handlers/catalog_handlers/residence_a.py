"""
Обработчик: Резиденция А
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .A_Residence.keyboards import get_residence_a_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_a")
async def residence_a_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция А"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция А</b>\n\n"
        "Тут будет текст\n\n"
        "Выберите интересующую вас информацию:",
        reply_markup=get_residence_a_keyboard()
    )


@router.callback_query(lambda c: c.data == "back_to_catalog")
async def back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Назад в каталог"
    Возвращает пользователя обратно в каталог резиденций
    """
    await callback.answer()

    # Сбрасываем состояние FSM
    await state.clear()

    # Импортируем клавиатуру каталога
    from .keyboards import get_catalog_keyboard

    # Отправляем каталог с кнопками резиденций
    await callback.message.answer(
        "🏢 <b>Каталог резиденций</b>\n\n"
        "Тут будет описание\n\n"
        "Выберите интересующую вас резиденцию:",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "back_to_main_menu")
async def back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Главное меню"
    Возвращает пользователя в главное меню как при /start
    """
    await callback.answer()

    # Сбрасываем состояние FSM
    await state.clear()

    # Импортируем клавиатуру и картинку
    from keyboards import get_main_menu_keyboard

    START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"

    # Отправляем картинку с главным меню
    await callback.message.answer_photo(
        photo=START_IMAGE_URL,
        caption="Я виртуальный помощник. Выберете пункт меню",
        reply_markup=get_main_menu_keyboard()
    )


