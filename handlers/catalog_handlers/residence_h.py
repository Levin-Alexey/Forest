"""
Обработчик: Резиденция З
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_h")
async def residence_h_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция З"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция З</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
