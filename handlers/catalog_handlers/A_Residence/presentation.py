"""
Обработчик: Получить презентацию (Резиденция А)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "a_presentation")
async def a_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции А
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции А</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
