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
]
