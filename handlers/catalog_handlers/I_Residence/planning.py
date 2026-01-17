"""
Обработчик: Планировка (Резиденция И)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "i_planning")
async def i_planning_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции И</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
