"""
Обработчик: Фотогаллерея (Резиденция З)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "h_photo_gallery")
async def h_photo_gallery_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции З</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
