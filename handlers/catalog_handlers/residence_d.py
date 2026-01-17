"""
Обработчик: Резиденция Г
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_d")
async def residence_d_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Г"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция Г</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
