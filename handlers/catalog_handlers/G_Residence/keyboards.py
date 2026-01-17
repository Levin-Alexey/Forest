"""
Клавиатуры для резиденции Ж
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_g_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции Ж
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="g_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="g_planning")],
            [InlineKeyboardButton(text="📝 Описание", callback_data="g_description")],
            [InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="g_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="g_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="g_back_to_main_menu")],
        ]
    )
    return keyboard
