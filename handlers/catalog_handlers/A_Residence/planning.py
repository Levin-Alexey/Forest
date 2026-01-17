"""
Обработчик: Планировка (Резиденция А)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "a_planning")
async def a_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции А
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции А</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
