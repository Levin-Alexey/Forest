"""
Обработчик: Резиденция А
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_a")
async def residence_a_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция А"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция А</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
