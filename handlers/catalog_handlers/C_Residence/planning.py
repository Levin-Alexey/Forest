"""
Обработчик: Планировка (Резиденция В)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "c_planning")
async def c_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции В
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции В</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
