"""
Обработчик: Планировка (Резиденция Г)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "d_planning")
async def d_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции Г
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции Г</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
