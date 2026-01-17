"""
Обработчик: Фотогаллерея (Резиденция Д)
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "e_photo_gallery")
async def e_photo_gallery_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Фотогаллерея" для резиденции Д
    """
    await callback.answer()
    await callback.message.answer(
        "🖼️ <b>Фотогаллерея Резиденции Д</b>\n\n"
        "⚙️ Функция в разработке\n\n"
        "Здесь будут фотографии резиденции, интерьеров и окружающей территории."
    )
