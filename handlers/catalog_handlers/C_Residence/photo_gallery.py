"""
Обработчик: Фотогаллерея (Резиденция В)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "c_photo_gallery")
async def c_photo_gallery_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Фотогаллерея" для резиденции В
    """
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции В</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
