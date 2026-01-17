"""
Клавиатуры для резиденции Б
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_b_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции Б
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="b_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="b_planning")],
            [InlineKeyboardButton(text="📝 Описание", callback_data="b_description")],
            [InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="b_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="b_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="b_back_to_main_menu")],
        ]
    )
    return keyboard
