"""
Обработчик: Резиденция А
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .A_Residence.keyboards import get_residence_a_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_a")
async def residence_a_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция А"
    """
    await callback.answer()
    await callback.message.answer(
        "<b>Резиденция в «Pisateli Forest» - ваш личный манифест комфорта и тишины.</b>\n\n"
        "Эта резиденция создана для тех, кто не готов к компромиссам. Здесь архитектурная эстетика встречается с инженерным совершенством, а интерьер уже готов к вашему приезду.\n\n"
        "🏠 <b>Краткие характеристики лота:</b>\n"
        "• Площадь резиденции: 240 м² \n"
        "• Участок: 6,8 сот. (базовое благоустройство уже выполнено)\n"
        "• Приватные зоны: 3 просторные спальни, включая мастер блок и 3 санузла\n"
        "• Пространство: Высота потолков 3.1 м — максимум света и воздуха\n"
        "• Паркинг: 4 машиноместа (с системой подогрева покрытия)\n"
        "• Готовность: Полная отделка «Под ключ»\n"
        "• Комплектация: Премиальная кухня с островом\n"
        "🎁 <b>ОСОБОЕ ПРЕДЛОЖЕНИЕ:</b> \n"
        "При покупке данной резиденции вы получаете полный комплект мягкой мебели в подарок! \n\n"
        "🔍 <b>Погрузитесь в детали проекта:</b>\n"
        "Эта карточка — лишь верхушка айсберга. Чтобы по-настоящему прочувствовать атмосферу, детали отделки и умные решения, которые скрыты от глаз, мы подготовили для вас несколько удобных инструментов:\n"
        "1.  🖼 <b>Раздел «Рендеры»:</b> Увидьте, как свет ложится на фактуры стен в разное время суток.\n"
        "2.  📐 <b>Раздел «Планировки»:</b> Изучите сценарии жизни — от тихих завтраков на террасе до приема гостей.\n"
        "3.  🤖 <b>Ваш AI-помощник:</b> Спросите его о чем угодно! «Какая система очистки воздуха в доме?», «Из чего сделан фундамент?» или «Какие школы есть рядом?». Наш ИИ знает о Pisateli Forest всё.\n\n"
        "📥 <b>Для самого глубокого изучения:</b> \n"
        "Нажмите кнопку «Скачать презентацию», чтобы получить полный PDF-каталог со всеми техническими деталями, спецификациями отделки и эксклюзивными фотографиями объекта.",
        parse_mode="HTML",
        reply_markup=get_residence_a_keyboard()
    )


@router.callback_query(lambda c: c.data == "back_to_catalog")
async def back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
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
        "🏢 Каталог резиденций\n\n"
        "Выберите интересующую Вас резиденцию:",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "back_to_main_menu")
async def back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
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


