"""
Клавиатуры для резиденции В
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_c_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции В
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="c_presentation")],
            #[InlineKeyboardButton(text="📐 Планировка", callback_data="c_planning")],
            #[InlineKeyboardButton(text="📝 Описание", callback_data="c_description")],
            #[InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="c_photo_gallery")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="c_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="c_back_to_main_menu")],
        ]
    )
    return keyboard
