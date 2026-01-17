"""
Обработчик: Получить презентацию (Резиденция К)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "k_presentation")
async def k_presentation_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции К</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
