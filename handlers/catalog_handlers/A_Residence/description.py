"""
Обработчик: Описание (Резиденция А)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "a_description")
async def a_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции А
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции А</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
