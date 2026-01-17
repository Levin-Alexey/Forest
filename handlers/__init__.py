"""
Обработчики для inline-кнопок бота
"""

from .ai_consultant import router as ai_consultant_router
from .about_project import router as about_project_router
from .catalog import router as catalog_router
from .video_review import router as video_review_router
from .contact_manager import router as contact_manager_router
from .links import router as links_router

# Импортируем роутеры резиденций из catalog_handlers
from .catalog_handlers import (
    residence_a_router,
    residence_b_router,
    residence_c_router,
    residence_d_router,
    residence_e_router,
    residence_f_router,
    residence_g_router,
    residence_h_router,
    residence_i_router,
    residence_k_router,
    # Роутеры резиденции А
    a_presentation_router,
    a_planning_router,
    a_description_router,
    a_photo_gallery_router,
    # Роутеры резиденции Б
    b_presentation_router,
    b_planning_router,
    b_description_router,
    b_photo_gallery_router,
    # Роутеры резиденции В
    c_presentation_router,
    c_planning_router,
    c_description_router,
    c_photo_gallery_router,
    # Роутеры резиденции Г
    d_presentation_router,
    d_planning_router,
    d_description_router,
    d_photo_gallery_router,
    # Роутеры резиденции Д
    e_presentation_router,
    e_planning_router,
    e_description_router,
    e_photo_gallery_router,
    # Роутеры резиденции Е
    f_presentation_router,
    f_planning_router,
    f_description_router,
    f_photo_gallery_router,
    # Роутеры резиденции Ж
    g_presentation_router,
    g_planning_router,
    g_description_router,
    g_photo_gallery_router,
    # Роутеры резиденции З
    h_presentation_router,
    h_planning_router,
    h_description_router,
    h_photo_gallery_router,
    # Роутеры резиденции И
    i_presentation_router,
    i_planning_router,
    i_description_router,
    i_photo_gallery_router,
    # Роутеры резиденции К
    k_presentation_router,
    k_planning_router,
    k_description_router,
    k_photo_gallery_router,
)

__all__ = [
    'ai_consultant_router',
    'about_project_router',
    'catalog_router',
    'video_review_router',
    'contact_manager_router',
    'links_router',
    # Роутеры резиденций
    'residence_a_router',
    'residence_b_router',
    'residence_c_router',
    'residence_d_router',
    'residence_e_router',
    'residence_f_router',
    'residence_g_router',
    'residence_h_router',
    'residence_i_router',
    'residence_k_router',
    # Роутеры резиденции А
    'a_presentation_router',
    'a_planning_router',
    'a_description_router',
    'a_photo_gallery_router',
    # Роутеры резиденции Б
    'b_presentation_router',
    'b_planning_router',
    'b_description_router',
    'b_photo_gallery_router',
    # Роутеры резиденции В
    'c_presentation_router',
    'c_planning_router',
    'c_description_router',
    'c_photo_gallery_router',
    # Роутеры резиденции Г
    'd_presentation_router',
    'd_planning_router',
    'd_description_router',
    'd_photo_gallery_router',
    # Роутеры резиденции Д
    'e_presentation_router',
    'e_planning_router',
    'e_description_router',
    'e_photo_gallery_router',
    # Роутеры резиденции Е
    'f_presentation_router',
    'f_planning_router',
    'f_description_router',
    'f_photo_gallery_router',
    # Роутеры резиденции Ж
    'g_presentation_router',
    'g_planning_router',
    'g_description_router',
    'g_photo_gallery_router',
    # Роутеры резиденции З
    'h_presentation_router',
    'h_planning_router',
    'h_description_router',
    'h_photo_gallery_router',
    # Роутеры резиденции И
    'i_presentation_router',
    'i_planning_router',
    'i_description_router',
    'i_photo_gallery_router',
    # Роутеры резиденции К
    'k_presentation_router',
    'k_planning_router',
    'k_description_router',
    'k_photo_gallery_router',
]
