"""
Обработчик: О проекте
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "about_project")
async def about_project_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "О проекте"
    """
    await callback.answer()
    await callback.message.answer("⚙️ Функция в разработке")
