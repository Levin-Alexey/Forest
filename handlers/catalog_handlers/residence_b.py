"""
Обработчик: Резиденция Б
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_b")
async def residence_b_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Б"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция Б</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
