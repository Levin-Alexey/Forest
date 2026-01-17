"""
Обработчик: Видеообзор шоурум
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "video_review")
async def video_review_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Видеообзор шоурум"
    """
    await callback.answer()
    await callback.message.answer("⚙️ Функция в разработке")
