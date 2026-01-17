"""
Обработчик: Связаться с менеджером
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "contact_manager")
async def contact_manager_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Связаться с менеджером"
    """
    await callback.answer()
    await callback.message.answer("⚙️ Функция в разработке")
