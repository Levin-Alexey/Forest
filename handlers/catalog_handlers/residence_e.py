"""
Обработчик: Резиденция Д
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .E_Residence.keyboards import get_residence_e_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_e")
async def residence_e_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Д"
    """
    await callback.answer()
    await callback.message.answer(
        "<b>Резиденция \"Д\" в «Pisateli Forest» — дом, в сердце которого живет природа</b>\n\n"
        "У этого лота есть уникальная особенность, которую крайне редко встретишь на рынке элитной недвижимости - <b>живая реликтовая сосна, интегрированная прямо в террасу дома</b>. Мы называем это «диким зверем»: архитектура не спорит с лесом, а обнимает его. Это не просто дом, это живой арт-объект.\n"
        "🚀 <b>Главная новость:</b> Дом почти готов! Покупая его сейчас, вы уже этим летом сможете устраивать первые барбекю-вечеринки в кругу семьи и друзей на собственной благоустроенной территории.\n"
        "🏠 <b>Характеристики лота:</b>\n"
        "• Площадь дома: 439 м² \n"
        "• Участок: 9 сот. \n"
        "• Уникальность: Живая сосна, проходящая сквозь террасу 🌲\n"
        "• Приватные зоны: 4 уютные спальни и 4 санузла\n"
        "• Комфорт: Высота потолков 3.2 м и панорамное остекление\n"
        "• Паркинг: 4 машиноместа (с подогревом покрытия)\n"
        "• Готовность: Полная отделка «Под ключ» + кухонный гарнитур с островом\n"
        "• Территория: Ландшафтное благоустройство уже выполнено\n"
        "🔎 <b>Исследуйте свой будущий дом:</b>\n"
        "1.  🖼 Раздел «Рендеры»: Посмотрите, как эффектно выглядит та самая сосна на террасе и как она меняет восприятие пространства.\n"
        "2.  📐 Раздел «Планировки»: Оцените удобство выхода из кухни к зоне барбекю.\n"
        "3.  🤖 Ваш AI-помощник: Спросите его: «Как реализована гидроизоляция вокруг дерева на террасе?» или «Сколько гардеробных в доме?».\n"
        "📥 <b>Узнать всё о резиденции:</b> \n"
        "Нажмите кнопку «Скачать презентацию», чтобы получить детальный PDF-каталог с техническими узлами, планами участка и фотографиями отделочных материалов. Ваше идеальное лето начинается здесь",
        parse_mode="HTML",
        reply_markup=get_residence_e_keyboard()
    )


@router.callback_query(lambda c: c.data == "e_back_to_catalog")
async def e_back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
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


@router.callback_query(lambda c: c.data == "e_back_to_main_menu")
async def e_back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
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
