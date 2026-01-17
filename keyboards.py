"""
Клавиатуры для бота
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Главное меню с inline-кнопками
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🤖 AI консультант",
                    callback_data="ai_consultant"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 О проекте",
                    callback_data="about_project"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏠 Каталог резиденций",
                    callback_data="catalog"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎥 Видеообзор шоурум",
                    callback_data="video_review"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👤 Связаться с менеджером",
                    callback_data="contact_manager"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌐 Сайт / Группа TG",
                    callback_data="links"
                )
            ],
        ]
    )
    return keyboard
