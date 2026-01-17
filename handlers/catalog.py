"""
Обработчик: Каталог резиденций
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from .catalog_handlers.keyboards import get_catalog_keyboard

router = Router()


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
async def back_to_menu_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Назад в меню"
    """
    await callback.answer()
    # TODO: Отправить пользователя обратно в главное меню
    await callback.message.answer("◀️ Возврат в главное меню...")

