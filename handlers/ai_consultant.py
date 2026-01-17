"""
Обработчик: AI консультант
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "ai_consultant")
async def ai_consultant_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "AI консультант"
    """
    await callback.answer()
    await callback.message.answer("⚙️ Функция в разработке")
