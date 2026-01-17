"""
Обработчик: Резиденция Е
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "residence_f")
async def residence_f_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Е"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция Е</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет описание резиденции, фотографии, цены и другая информация."
    )
