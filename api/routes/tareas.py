from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from ..schemas import schemas

from .. import crud
from ..database import get_db

# Se define un enrutador con prefijo /tareas y etiqueta para documentación Swagger
router = APIRouter(prefix="/tareas", tags=["Tareas"])

# Endpoint para crear una nueva tarea (POST /tareas/)
@router.post("/", response_model=schemas.TareaOut)
def crear(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    return crud.crear_tarea(db, tarea)

# Endpoint para listar todas las tareas o una sola si se proporciona tarea_id (GET /tareas/)
@router.get("/", response_model=list[schemas.TareaOut])
def listar_o_obtener(tarea_id: Optional[int] = None, db: Session = Depends(get_db)):
    if tarea_id is not None:
        tarea = crud.obtener_tarea(db, tarea_id)
        if not tarea:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return [tarea]
    return crud.obtener_todas(db)

# Endpoint para crear varias tareas en una sola petición (POST /tareas/masivo)
@router.post("/masivo", response_model=list[schemas.TareaOut])
def crear_masivo(tareas: list[schemas.TareaCreate], db: Session = Depends(get_db)):
    resultados = []
    for tarea in tareas:
        nueva = crud.crear_tarea(db, tarea)
        resultados.append(nueva)
    return resultados

# Endpoint para actualizar una tarea existente por ID usando un parámetro en la URL (PUT /tareas/?tarea_id=...)
@router.put("/", response_model=schemas.TareaOut)
def actualizar(tarea_id: int, tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    actualizada = crud.actualizar_tarea(db, tarea_id, tarea)
    if not actualizada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return actualizada

# Endpoint para eliminar una tarea por ID usando un parámetro (DELETE /tareas/?tarea_id=...)
@router.delete("/")
def eliminar(tarea_id: int, db: Session = Depends(get_db)):
    eliminada = crud.eliminar_tarea(db, tarea_id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"msg": "Tarea eliminada"}

# Endpoint para listar tareas por estado (GET /tareas/estado?estado=...)
@router.get("/estado", response_model=list[schemas.TareaOut])
def listar_por_estado(estado: str, db: Session = Depends(get_db)):
    tareas = crud.obtener_por_estado(db, estado)
    if not tareas:
        raise HTTPException(status_code=404, detail="No hay tareas con ese estado")
    return tareas
