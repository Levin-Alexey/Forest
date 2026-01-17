"""
Обработчик: Планировка (Резиденция З)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "h_planning")
async def h_planning_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции З</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
