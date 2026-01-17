"""
Обработчик: Описание (Резиденция И)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "i_description")
async def i_description_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции И</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
