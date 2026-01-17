"""
Обработчик: Планировка (Резиденция К)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "k_planning")
async def k_planning_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции К</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
