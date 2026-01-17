"""
Обработчик: Фотогаллерея (Резиденция К)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "k_photo_gallery")
async def k_photo_gallery_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции К</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
