"""
Обработчик: Резиденция Д
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_e")
async def residence_e_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Д"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция Д</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
