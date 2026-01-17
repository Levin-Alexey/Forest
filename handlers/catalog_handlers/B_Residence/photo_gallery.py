"""
Обработчик: Фотогаллерея (Резиденция Б)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "b_photo_gallery")
async def b_photo_gallery_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Фотогаллерея" для резиденции Б
    """
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции Б</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
