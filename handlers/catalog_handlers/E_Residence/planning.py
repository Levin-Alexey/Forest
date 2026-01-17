"""
Обработчик: Планировка (Резиденция Д)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "e_planning")
async def e_planning_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Планировка" для резиденции Д
    """
    await callback.answer()
    await callback.message.answer(
        "📐 <b>Планировка Резиденции Д</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут показаны планы этажей и квартир."
    )
