"""
Обработчики для резиденций в каталоге
"""

from .residence_a import router as residence_a_router
from .residence_b import router as residence_b_router
from .residence_c import router as residence_c_router
from .residence_d import router as residence_d_router
from .residence_e import router as residence_e_router
from .residence_f import router as residence_f_router
from .residence_g import router as residence_g_router
from .residence_h import router as residence_h_router
from .residence_i import router as residence_i_router
from .residence_k import router as residence_k_router

# Импортируем роутеры обработчиков резиденции А
from .A_Residence import (
    presentation_router as a_presentation_router,
    planning_router as a_planning_router,
    description_router as a_description_router,
    photo_gallery_router as a_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции Б
from .B_Residence import (
    presentation_router as b_presentation_router,
    planning_router as b_planning_router,
    description_router as b_description_router,
    photo_gallery_router as b_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции В
from .C_Residence import (
    presentation_router as c_presentation_router,
    planning_router as c_planning_router,
    description_router as c_description_router,
    photo_gallery_router as c_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции Г
from .D_Residence import (
    presentation_router as d_presentation_router,
    planning_router as d_planning_router,
    description_router as d_description_router,
    photo_gallery_router as d_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции Д
from .E_Residence import (
    presentation_router as e_presentation_router,
    planning_router as e_planning_router,
    description_router as e_description_router,
    photo_gallery_router as e_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции Е
from .F_Residence import (
    presentation_router as f_presentation_router,
    planning_router as f_planning_router,
    description_router as f_description_router,
    photo_gallery_router as f_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции Ж
from .G_Residence import (
    presentation_router as g_presentation_router,
    planning_router as g_planning_router,
    description_router as g_description_router,
    photo_gallery_router as g_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции З
from .H_Residence import (
    presentation_router as h_presentation_router,
    planning_router as h_planning_router,
    description_router as h_description_router,
    photo_gallery_router as h_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции И
from .I_Residence import (
    presentation_router as i_presentation_router,
    planning_router as i_planning_router,
    description_router as i_description_router,
    photo_gallery_router as i_photo_gallery_router,
)

# Импортируем роутеры обработчиков резиденции К
from .K_Residence import (
    presentation_router as k_presentation_router,
    planning_router as k_planning_router,
    description_router as k_description_router,
    photo_gallery_router as k_photo_gallery_router,
)

__all__ = [
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
