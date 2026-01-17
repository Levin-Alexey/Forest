"""
Обработчик: Описание (Резиденция Б)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "b_description")
async def b_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции Б
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции Б</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
