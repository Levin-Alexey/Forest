"""
Обработчик: Фотогаллерея (Резиденция А)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "a_photo_gallery")
async def a_photo_gallery_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Фотогаллерея" для резиденции А
    """
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции А</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
