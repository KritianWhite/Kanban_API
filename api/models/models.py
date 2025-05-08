from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func
import enum

from ..database import Base

# Class Enumeración para los estados de una tarea en el tablero Kanban
class EstadoTarea(str, enum.Enum):
    backlog = "BACKLOG"
    progreso = "EN_PROGRESO"
    hecho = "HECHO"
    archivado = "ARCHIVADO"

# Class Enumeración para los niveles de prioridad de una tarea
class PrioridadTarea(str, enum.Enum):
    baja = "BAJA"
    media = "MEDIA"
    alta = "ALTA"
    urgente = "URGENTE"

# Modelo ORM que representa la tabla 'tareas' en la base de datos
class Tarea(Base):
    __tablename__ = "tareas"    # Nombre de la tabla en la base de datos

    # Definición de las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True) # ID de la tarea, clave primaria
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    estado = Column(Enum(EstadoTarea), default=EstadoTarea.backlog)
    prioridad = Column(Enum(PrioridadTarea), default=PrioridadTarea.media)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
