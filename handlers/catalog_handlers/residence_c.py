"""
Обработчик: Резиденция В
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_c")
async def residence_c_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция В"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция В</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
