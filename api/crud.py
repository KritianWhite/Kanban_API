from sqlalchemy.orm import Session

from .schemas import schemas

from .models import models

# Crear una nueva tarea en la base de datos
def crear_tarea(db: Session, tarea: schemas.TareaCreate):
    # Convertir el esquema en un objeto del modelo
    nueva = models.Tarea(**tarea.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# Obtener una tarea específica por su ID
def obtener_tarea(db: Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

# Obtener todas las tareas registradas
def obtener_todas(db: Session):
    return db.query(models.Tarea).all()

# Actualizar una tarea existente con los nuevos datos recibidos
def actualizar_tarea(db: Session, tarea_id: int, tarea: schemas.TareaCreate):
    db_tarea = obtener_tarea(db, tarea_id)
    if db_tarea:
        for key, value in tarea.dict().items():
            setattr(db_tarea, key, value)
        db.commit()
        db.refresh(db_tarea)
    return db_tarea

# Eliminar una tarea existente por su ID
def eliminar_tarea(db: Session, tarea_id: int):
    db_tarea = obtener_tarea(db, tarea_id)
    if db_tarea:
        db.delete(db_tarea)
        db.commit()
    return db_tarea

# Obtener tareas por su estado
def obtener_por_estado(db: Session, estado: str):
    return db.query(models.Tarea).filter(models.Tarea.estado == estado).all()
