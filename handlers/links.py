"""
Обработчик: Сайт / Группа TG
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "links")
async def links_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Сайт / Группа TG"
    """
    await callback.answer()
    await callback.message.answer("⚙️ Функция в разработке")
