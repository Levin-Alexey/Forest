"""
Обработчик: Получить презентацию (Резиденция В)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "c_presentation")
async def c_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции В
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции В</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
