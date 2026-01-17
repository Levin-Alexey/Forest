"""
Обработчик: Резиденция Ж
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_g")
async def residence_g_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Ж"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция Ж</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
