"""
Обработчик: Планировка (Резиденция Б)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "b_planning")
async def b_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции Б
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции Б</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
