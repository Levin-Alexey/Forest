"""
Обработчик: Резиденция И
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_i")
async def residence_i_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция И"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция И</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
