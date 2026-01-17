"""
Обработчик: Получить презентацию (Резиденция З)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "h_presentation")
async def h_presentation_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции З</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
