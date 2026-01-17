"""
Обработчик: Описание (Резиденция З)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "h_description")
async def h_description_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции З</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
