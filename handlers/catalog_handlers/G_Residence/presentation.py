"""
Обработчик: Получить презентацию (Резиденция Ж)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "g_presentation")
async def g_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции Ж
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции Ж</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
