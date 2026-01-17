"""
Обработчики для inline-кнопок бота
"""

from .ai_consultant import router as ai_consultant_router
from .about_project import router as about_project_router
from .catalog import router as catalog_router
from .video_review import router as video_review_router
from .contact_manager import router as contact_manager_router
from .links import router as links_router

__all__ = [
    'ai_consultant_router',
    'about_project_router',
    'catalog_router',
    'video_review_router',
    'contact_manager_router',
    'links_router',
]
