"""
Обработчик: Видеообзор шоурум
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "video_review")
async def video_review_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Видеообзор шоурум"
    """
    await callback.answer()
    await callback.message.answer(
        "Приглашаем вас на виртуальную прогулку по PISATELI FOREST. 🌲\n\n"
        "Чтобы вы могли оценить архитектуру, масштаб остекления и качество каждой детали, "
        "мы подготовили подробный видеообзор одной из готовых резиденций.\n\n"
        "📽 Смотреть обзор (ВК Видео)\n"
        "*(здесь будет ваша ссылка)*\n\n"
        "Наслаждайтесь просмотром! А если после видео у вас возникнет желание увидеть всё вживую "
        "или узнать детали покупки - я помогу мгновенно связаться с менеджером"
    )
