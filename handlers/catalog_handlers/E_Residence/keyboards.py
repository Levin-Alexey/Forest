"""
Клавиатуры для резиденции Д
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_e_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции Д
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="e_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="e_planning")],
            [InlineKeyboardButton(text="📝 Описание", callback_data="e_description")],
            [InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="e_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="e_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="e_back_to_main_menu")],
        ]
    )
    return keyboard
