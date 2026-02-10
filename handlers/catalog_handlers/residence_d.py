"""
Обработчик: Резиденция Г
"""
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .D_Residence.keyboards import get_residence_d_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "residence_d")
async def residence_d_handler(callback: CallbackQuery):
    """
    Обработчик кнопки "Резиденция Г"
    """
    await callback.answer()
    await callback.message.answer(
        "🏠 <b>Резиденция Г</b>\n\n"
        "Тут будет текст\n\n"
        "Выберите интересующую вас информацию:",
        reply_markup=get_residence_d_keyboard()
    )


@router.callback_query(lambda c: c.data == "d_back_to_catalog")
async def d_back_to_catalog_handler(callback: CallbackQuery, state: FSMContext):
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
        "<b>Благодарю за интерес к «Pisateli Forest». Вы на пороге выбора резиденции, где премиальный комфорт "
        "уже заложен в основу каждой детали.</b>\n\n"
        "Мы понимаем, что покупка дома — это только начало пути. Чтобы избавить вас от сложностей ремонта и поиска подрядчиков, "
        "мы разработали стандарт «Ready for life».\n\n"
        "<b>Вот что уже ВКЛЮЧЕНО в базовую стоимость каждой резиденции:</b>\n"
        "• <b>Полная чистовая отделка:</b> Высококачественные материалы, безупречное исполнение и эстетика современного загородного дома.\n"
        "• <b>Инженерный фундамент комфорта:</b> Система многоступенчатой очистки воздуха, теплые полы, скрытое управление климатом "
        "и подогрев всех входных групп (крыльцо, парковочные места).\n"
        "• <b>Сердце дома:</b> Установленный дровяной камин и полностью укомплектованный кухонный гарнитур.\n"
        "• <b>Приватная территория:</b> Забор в едином стиле поселка, автоматические ворота, базовое благоустройство участка.\n\n"
        "✨ <b>Это - лишь малая часть «фишек» проекта</b>\n\n"
        "Перечислить всё невозможно, да и вряд ли текст передаст ощущение от тактильных материалов, аромата хвои в панорамных окнах "
        "или того, как инженерные системы работают в идеальном тандеме. <b>Это тот случай, когда лучше один раз увидеть всё своими глазами, "
        "чем изучать списки характеристик.</b> Каждая деталь в «Pisateli Forest» создана, чтобы удивлять при личной встрече.\n\n"
        "🏠 <b>Индивидуальный подход «Под тапочки»:</b>\n\n"
        "Если вы цените максимальную готовность, мы можем пойти дальше. Мы укомплектуем резиденцию мебелью и аксессуарами — "
        "либо строго по авторскому дизайн-проекту, либо адаптируем интерьер под ваши личные пожелания, "
        "чтобы ваш переезд стал легким и приятным.\n\n"
        "<b>В нашем каталоге представлены лоты разной конфигурации:</b>\n"
        "• Площадь от 240 до 536 м² (участки 6–10 соток).\n"
        "• От 3 до 5 спален с продуманными мастер-зонами.\n\n"
        "<b>Ознакомьтесь с актуальными предложениями ниже.</b>",
        parse_mode="HTML",
        reply_markup=get_catalog_keyboard()
    )


@router.callback_query(lambda c: c.data == "d_back_to_main_menu")
async def d_back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
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
