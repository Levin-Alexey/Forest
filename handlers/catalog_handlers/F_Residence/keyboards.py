"""
Клавиатуры для резиденции Е
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_f_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции Е
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="f_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="f_planning")],
            [InlineKeyboardButton(text="📝 Описание", callback_data="f_description")],
            [InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="f_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="f_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="f_back_to_main_menu")],
        ]
    )
    return keyboard
