"""
Обработчик: Описание (Резиденция Ж)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "g_description")
async def g_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции Ж
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции Ж</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
