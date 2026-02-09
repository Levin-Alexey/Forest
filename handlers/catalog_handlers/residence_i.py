"""
Обработчик: Резиденция И
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .I_Residence.keyboards import get_residence_i_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_i")
async def residence_i_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция И"
    """
    await callback.answer()
    await callback.message.answer(
        "<b>Резиденция 475 в «Pisateli Forest» — дом, где лес становится частью интерьера.</b>\n"
        "Главная ценность этого лота - уникальный, неизменный круглогодичный вид. Пока другие пейзажи меняются с сезонами, ваши окна всегда смотрят на плотную, живую стену вековых елей. Это ваш личный хвойный замок, который остается идеально зеленым и летом, и заснеженной зимой.\n"
        "🌲 <b>Почему этот дом влюбляет в себя:</b>\n"
        "• <b>Вид «миллион на миллион»:</b> Панорамные окна спален выходят прямо на стену из елей. Вы просыпаетесь, видя только бесконечную зелень.\n"
        "• <b>Приватная терраса мастер-блока:</b> Уникальное пространство, где можно буквально коснуться лап елок, не выходя из дома.\n"
        "• <b>Живая природа:</b> Здесь природа по-настоящему близко. На ветви прямо перед вашими окнами прилетают совы и филины, а белки — постоянные гости вашей террасы.\n"
        "• <b>Forest-view BBQ:</b> Вся зона отдыха на заднем дворе и барбекю-площадка развернуты к лесу, создая ощущение полной изоляции от внешнего мира.\n"
        "• <b>Релакс-зона:</b> Собственный SPA-блок для восстановления сил в окружении тишины.\n"
        "🏠 <b>Характеристики лота:</b>\n"
        "• Площадь дома: 475 м²\n"
        "• Участок: 7,5 сот. (с полным благоустройством)\n"
        "• Высота потолков: 3,3 м\n"
        "• Спальни: 4 уютные спальни с лучшими видами в посёлке.\n"
        "• Санузлы: 4 ванные комнаты.\n"
        "• Готовность: «Под ключ» с премиальной отделкой и дизайнерской кухней с островом.\n"
        "• Паркинг: 4 машиноместа.\n"
        "🕵️ <b>Посмотрите на этот дом глазами владельца:</b>\n"
        "1.  🖼 <b>Раздел «Рендеры»:</b> Оцените вид из окон спален — вы увидите ту самую «зеленую стену», которая будет радовать вас 365 дней в году.\n"
        "2.  📐 <b>Раздел «Планировки»:</b> Изучите мастер-блок с его уникальной террасой и посмотрите, как грамотно вписан SPA-блок в общую логику дома.\n"
        "3.  🤖 <b>Ваш AI-помощник:</b> Спросите его: «Какие птицы прилетают к террасе мастер-блока?» или «Как организована зона барбекю относительно леса?».\n"
        "---\n"
        "📥 <b>Получить эксклюзивные материалы:</b> \n"
        "Нажмите кнопку «Скачать презентацию», чтобы увидеть фотографии вида из окон и подробные спецификации отделки этой лесной резиденции.",
        parse_mode="HTML",
        reply_markup=get_residence_i_keyboard()
    )


@router.callback_query(lambda c: c.data == "i_back_to_catalog")
async def i_back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Назад в каталог"
    Возвращает пользователя обратно в каталог резиденций
    """
    await callback.answer()
    await state.clear()
    from .keyboards import get_catalog_keyboard
    await callback.message.answer(
        "🏢 Каталог резиденций\n\n"
        "Выберите интересующую Вас резиденцию:",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "i_back_to_main_menu")
async def i_back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Главное меню"
    Возвращает пользователя в главное меню как при /start
    """
    await callback.answer()
    await state.clear()
    from keyboards import get_main_menu_keyboard
    START_IMAGE_URL = "https://optim.tildacdn.com/tild3535-3863-4331-b136-396632393536/-/format/webp/IMG_1358.png.webp"
    await callback.message.answer_photo(
        photo=START_IMAGE_URL,
        caption="Я виртуальный помощник. Выберете пункт меню",
        reply_markup=get_main_menu_keyboard()
    )
