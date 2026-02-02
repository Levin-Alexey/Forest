"""
Клавиатуры для резиденции А
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_a_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для резиденции А
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="a_presentation")],
            #[InlineKeyboardButton(text="📐 Планировка", callback_data="a_planning")],
            #[InlineKeyboardButton(text="🖼️ Фотогаллерея", callback_data="a_photo_gallery")],
            [InlineKeyboardButton(text="🤖 AI Консультант", callback_data="ai_consultant")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="back_to_main_menu")],
        ]
    )
    return keyboard


