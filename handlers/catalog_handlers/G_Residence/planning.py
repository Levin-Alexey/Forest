"""
Обработчик: Планировка (Резиденция Ж)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "g_planning")
async def g_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции Ж
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции Ж</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
