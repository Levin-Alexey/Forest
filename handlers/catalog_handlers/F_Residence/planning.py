"""
Обработчик: Планировка (Резиденция Е)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "f_planning")
async def f_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции Е
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции Е</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
