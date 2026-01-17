"""
Клавиатура резиденции З
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_h_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="h_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="h_planning")],
            [InlineKeyboardButton(text="📝 Описание", callback_data="h_description")],
            [InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="h_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="h_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="h_back_to_main_menu")],
        ]
    )
