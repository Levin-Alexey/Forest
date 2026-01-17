"""
Обработчик: Описание (Резиденция К)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "k_description")
async def k_description_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции К</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
