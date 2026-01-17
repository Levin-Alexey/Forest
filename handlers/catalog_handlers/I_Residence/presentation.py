"""
Обработчик: Получить презентацию (Резиденция И)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "i_presentation")
async def i_presentation_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📊 <b>Презентация Резиденции И</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будет возможность скачать или просмотреть презентацию проекта."
    )
