"""
Клавиатуры для каталога резиденций
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_catalog_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура со всеми резиденциями
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🏠 Резиденция А", callback_data="residence_a")],
            [InlineKeyboardButton(text="🏠 Резиденция Б", callback_data="residence_b")],
            [InlineKeyboardButton(text="🏠 Резиденция В", callback_data="residence_c")],
            [InlineKeyboardButton(text="🏠 Резиденция Г", callback_data="residence_d")],
            [InlineKeyboardButton(text="🏠 Резиденция Д", callback_data="residence_e")],
            [InlineKeyboardButton(text="🏠 Резиденция Е", callback_data="residence_f")],
            [InlineKeyboardButton(text="🏠 Резиденция Ж", callback_data="residence_g")],
            [InlineKeyboardButton(text="🏠 Резиденция З", callback_data="residence_h")],
            [InlineKeyboardButton(text="🏠 Резиденция И", callback_data="residence_i")],
            [InlineKeyboardButton(text="🏠 Резиденция К", callback_data="residence_k")],
            [InlineKeyboardButton(text="◀️ Назад в меню", callback_data="back_to_menu")],
        ]
    )
    return keyboard
