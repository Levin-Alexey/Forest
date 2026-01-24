"""
Обработчик: Сайт / Группа TG
"""
from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


@router.callback_query(lambda c: c.data == "links")
async def links_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Сайт / Группа TG"
    """
    await callback.answer()
    
    # Создаем клавиатуру с кнопками-ссылками
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🌐 Наш сайт", url="https://pisateli-forest.ru/")],
            [InlineKeyboardButton(text="📱 Наша группа в ТГ", url="https://pisateli-forest.ru/")],
        ]
    )
    
    await callback.message.answer(
        "Выберите удобный формат знакомства с проектом:\n\n"
        "🌐 <b>Сайт</b> - эстетика, детальные планировки и визуальный подбор лота.\n"
        "🏗 <b>Telegram</b> - жизнь стройки в реальном времени, новости и наш лайфстайл.\n\n"
        "Будьте в курсе всех событий!",
        parse_mode="HTML",
        reply_markup=keyboard
    )
