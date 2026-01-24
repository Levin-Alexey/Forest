"""
Клавиатура резиденции И
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_residence_i_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Получить презентацию", callback_data="i_presentation")],
            [InlineKeyboardButton(text="📐 Планировка", callback_data="i_planning")],
            [InlineKeyboardButton(text="�️ Фотогаллерея", callback_data="i_photo_gallery")],
            [InlineKeyboardButton(text="🤖 AI Консультант", callback_data="ai_consultant")],
            [InlineKeyboardButton(text="◀️ Назад в каталог", callback_data="i_back_to_catalog")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="i_back_to_main_menu")],
        ]
    )
