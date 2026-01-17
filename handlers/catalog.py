"""
Обработчик: Каталог резиденций
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "catalog")
async def catalog_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Каталог резиденций"
    """
    await callback.answer()
    await callback.message.answer("⚙️ Функция в разработке")
