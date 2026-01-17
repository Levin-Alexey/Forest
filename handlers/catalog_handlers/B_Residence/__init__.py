"""
Обработчики для резиденции Б
"""

from .presentation import router as presentation_router
from .planning import router as planning_router
from .description import router as description_router
from .photo_gallery import router as photo_gallery_router

__all__ = [
    'presentation_router',
    'planning_router',
    'description_router',
    'photo_gallery_router',
]
