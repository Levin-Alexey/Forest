"""
Обработчик: Получить презентацию (Резиденция Б)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "b_presentation")
async def b_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции Б
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции Б</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
