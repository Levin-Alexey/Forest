"""
Обработчик: Описание (Резиденция В)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "c_description")
async def c_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции В
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции В</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
