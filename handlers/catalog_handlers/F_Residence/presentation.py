"""
Обработчик: Получить презентацию (Резиденция Е)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "f_presentation")
async def f_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции Е
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции Е</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
