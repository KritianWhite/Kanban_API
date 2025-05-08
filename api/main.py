from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text

from api.database import Base, engine, SessionLocal
from api.routes import tareas

# Crear todas las tablas definidas en los modelos (si no existen ya en la base de datos)
Base.metadata.create_all(bind=engine)

# Instancia principal de la API
app = FastAPI()

# Endpoint raíz para verificar que la API está activa y la conexión a la base es exitosa
@app.get("/", tags=["Sistema"])
def raiz():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # Consulta de prueba
        return JSONResponse(status_code=200, content={
            "mensaje": "API Kanban activa y funcionando correctamente.",
            "conexion_bd": "exitosa"
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "mensaje": "API activa, pero sin conexión a base de datos.",
            "error": str(e)
        })
    finally:
        db.close()

# Se incluye el router de tareas bajo el prefijo /tareas
app.include_router(tareas.router)  
