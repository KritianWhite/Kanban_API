from pydantic import BaseModel
from typing import Optional

from ..models.models import EstadoTarea, PrioridadTarea

# Esquema base que define los atributos comunes de una tarea
class TareaBase(BaseModel):
    titulo: str               # Título de la tarea (obligatorio) 
    descripcion: Optional[str] = None
    estado: EstadoTarea = EstadoTarea.backlog           # Estado por defecto: BACKLOG
    prioridad: PrioridadTarea = PrioridadTarea.media    # Prioridad por defecto: MEDIA

# Esquema usado al crear una tarea
class TareaCreate(TareaBase):
    pass

# Esquema usado para devolver una tarea desde la base de datos
class TareaOut(TareaBase):
    id: int

    class Config:
        orm_mode = True
