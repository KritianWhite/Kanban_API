from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargar las variables definidas en el archivo .env al entorno del sistema
load_dotenv()

# Obtener las variables necesarias para conectarse a la base de datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

#Construir la URL de conexión para la base de datos PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor de conexión con la base de datos
engine = create_engine(DATABASE_URL)

# Crear una clase de sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir una clase base de la cual heredarán todos los modelos ORM
Base = declarative_base()

# Función generadora que proporciona una sesión de base de datos a los endpoints del API
def get_db():
    # Se crea una sesión a la base de datos
    db = SessionLocal()
    try:
        # Devuelve la sesión para ser usada en una dependencia
        yield db
    finally:
        # Cierra la sesión después de su uso
        db.close()
