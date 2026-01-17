"""
Обработчик: Получить презентацию (Резиденция Г)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "d_presentation")
async def d_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции Г
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции Г</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
