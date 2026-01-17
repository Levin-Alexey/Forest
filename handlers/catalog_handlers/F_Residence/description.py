"""
Обработчик: Описание (Резиденция Е)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "f_description")
async def f_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции Е
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции Е</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
