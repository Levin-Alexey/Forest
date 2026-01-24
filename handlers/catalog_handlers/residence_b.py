"""
Обработчик: Резиденция Б
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .B_Residence.keyboards import get_residence_b_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_b")
async def residence_b_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Б"
    """
    await callback.answer()
    await callback.message.answer(
        "<b>Резиденция \"Б\" в «Pisateli Forest» - архитектурная доминанта и ваш личный курорт.</b>\n\n"
        "Это дом впечатляющих масштабов, где каждый элемент подчеркивает статус владельца. От собственного SPA-комплекса до гостиной с захватывающей дух высотой потолков — здесь всё создано для жизни в стиле «Extra Luxury».\n\n"
        "🏠 <b>Характеристики флагманской резиденции:</b>\n"
        "• Площадь дома: 530 м² (максимум пространства для жизни и отдыха)\n"
        "• Участок: 7,8 сот. (с готовым благоустройством)\n"
        "• Объем: Высота потолков от 3.3 до 7 метров («второй свет»)\n"
        "• Приватные зоны: 4 мастер-спальни и 5 санузлов\n"
        "• Relax-зона: Собственный SPA-блок внутри дома\n"
        "• Паркинг: 4 машиноместа с подогревом\n"
        "• Готовность: Полная отделка «Под ключ»\n"
        "• Комплектация: Дизайнерская кухня с островом\n"
        "✨ <b>Почувствуйте масштаб через детали:</b>\n"
        "Чтобы оценить грандиозность этой резиденции, воспользуйтесь нашими инструментами:\n"
        "1.  🖼 Раздел «Рендеры»: Посмотрите, как выглядят 7-метровые потолки и панорамное остекление в интерьере.\n"
        "2.  📐 Раздел «Планировки»: Изучите грамотное зонирование — как отделен SPA-блок от жилых комнат и как расположены гостевые зоны.\n"
        "3.  🤖 Ваш AI-помощник: Задайте сложные технические вопросы. Например: «Какие сценарии освещения предусмотрены в гостиной со вторым светом?» или «Какое оборудование установлено в SPA-зоне?».\n"
        "📥 <b>Полное досье объекта:</b> \n"
        "Нажмите кнопку «Скачать презентацию», чтобы получить PDF-файл со всеми планировочными решениями, детальной спецификацией отделки и инженерными характеристиками этой уникальной резиденции.",
        parse_mode="HTML",
        reply_markup=get_residence_b_keyboard()
    )


@router.callback_query(lambda c: c.data == "b_back_to_catalog")
async def b_back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Назад в каталог"
    Возвращает пользователя обратно в каталог резиденций
    """
    await callback.answer()

    # Сбрасываем состояние FSM
    await state.clear()

    # Импортируем клавиатуру каталога
    from .keyboards import get_catalog_keyboard

    # Отправляем каталог с кнопками резиденций
    await callback.message.answer(
        "🏢 <b>Каталог резиденций</b>\n\n"
        "Тут будет описание\n\n"
        "Выберите интересующую вас резиденцию:",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "b_back_to_main_menu")
async def b_back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Главное меню"
    Возвращает пользователя в главное меню как при /start
    """
    await callback.answer()

    # Сбрасываем состояние FSM
    await state.clear()

    # Импортируем клавиатуру и картинку
    from keyboards import get_main_menu_keyboard

    START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"

    # Отправляем картинку с главным меню
    await callback.message.answer_photo(
        photo=START_IMAGE_URL,
        caption="Я виртуальный помощник. Выберете пункт меню",
        reply_markup=get_main_menu_keyboard()
    )
