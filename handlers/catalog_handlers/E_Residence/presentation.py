"""
Обработчик: Получить презентацию (Резиденция Д)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "e_presentation")
async def e_presentation_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Получить презентацию" для резиденции Д
    """
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции Д</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
