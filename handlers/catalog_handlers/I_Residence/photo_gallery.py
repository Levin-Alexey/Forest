"""
Обработчик: Фотогаллерея (Резиденция И)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "i_photo_gallery")
async def i_photo_gallery_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции И</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
