"""
Обработчик: Описание (Резиденция Г)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "d_description")
async def d_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции Г
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции Г</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
