"""
Клавиатуры для резиденции Г
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_d_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции Г
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="d_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="d_planning")],
            [InlineKeyboardButton(text="📝 Описание", callback_data="d_description")],
            [InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="d_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="d_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="d_back_to_main_menu")],
        ]
    )
    return keyboard
