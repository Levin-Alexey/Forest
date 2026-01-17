"""
Обработчик: Резиденция К
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_k")
async def residence_k_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция К"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция К</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
