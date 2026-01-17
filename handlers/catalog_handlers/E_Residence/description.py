"""
Обработчик: Описание (Резиденция Д)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "e_description")
async def e_description_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Описание" для резиденции Д
    """
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Описание Резиденции Д</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет подробное описание особенностей, инфраструктуры и преимуществ резиденции."
    )
