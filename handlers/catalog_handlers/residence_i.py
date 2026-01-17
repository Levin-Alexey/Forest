"""
Обработчик: Резиденция И
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .I_Residence.keyboards import get_residence_i_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_i")
async def residence_i_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция И"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция И</b>\n\n"
        "Тут будет текст\n\n"
        "Выберите интересующую вас информацию:",
        reply_markup=get_residence_i_keyboard()
    )


@router.callback_query(lambda c: c.data == "i_back_to_catalog")
async def i_back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Назад в каталог"
    Возвращает пользователя обратно в каталог резиденций
    """
    await callback.answer()
    await state.clear()
    from .keyboards import get_catalog_keyboard
    await callback.message.answer(
        "🏢 <b>Каталог резиденций</b>\n\n"
        "Тут будет описание\n\n"
        "Выберите интересующую вас резиденцию:",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "i_back_to_main_menu")
async def i_back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Главное меню"
    Возвращает пользователя в главное меню как при /start
    """
    await callback.answer()
    await state.clear()
    from keyboards import get_main_menu_keyboard
    START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"
    await callback.message.answer_photo(
        photo=START_IMAGE_URL,
        caption="Я виртуальный помощник. Выберете пункт меню",
        reply_markup=get_main_menu_keyboard()
    )
