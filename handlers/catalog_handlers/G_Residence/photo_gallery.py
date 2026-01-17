"""
Обработчик: Фотогаллерея (Резиденция Ж)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "g_photo_gallery")
async def g_photo_gallery_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Фотогаллерея" для резиденции Ж
    """
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции Ж</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
