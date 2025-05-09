# Kanban API

API RESTful para la gestión de tareas estilo Kanban, desarrollada con FastAPI y PostgreSQL.

## Requisitos previos

- Python 3.10 o superior
- Git
- PostgreSQL (local o remoto)
- (Opcional) Entorno virtual

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/KritianWhite/Kanban_API.git
cd Kanban_API
```

2. Crear y activar un entorno virtual:

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```
ó:
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=kanban_db
```

En este caso se utilizó una base de datos creada en la nube.

5. Ejecutar la aplicación:

```bash
uvicorn api.main:app --reload
```

Acceso a la documentación automática: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints disponibles

### `GET /`

Verifica que la API esté activa y que la conexión a la base de datos sea exitosa.

**Respuesta esperada:**
```json
{
  "mensaje": "API Kanban activa y funcionando correctamente.",
  "conexion_bd": "exitosa"
}
```

### `POST /tareas/`

Crea una nueva tarea.

**Body (JSON):**
```json
{
  "titulo": "Diseñar logo",
  "descripcion": "Crear el logo para la app",
  "estado": "BACKLOG",
  "prioridad": "MEDIA"
}
```

### `POST /tareas/masivo`

Crea múltiples tareas a la vez.

**Body (JSON):**
```json
[
  {
    "titulo": "Conectar frontend",
    "descripcion": "Integrar React con la API",
    "estado": "EN_PROGRESO",
    "prioridad": "ALTA"
  },
  {
    "titulo": "Testear endpoints",
    "descripcion": "Validar respuestas HTTP",
    "estado": "HECHO",
    "prioridad": "MEDIA"
  }
]
```

### `GET /tareas/`

Lista todas las tareas registradas.

### `GET /tareas/?tarea_id=1`

Obtiene la tarea con ID específico.

### `GET /tareas/estado?estado=HECHO`

Obtiene todas las tareas con un estado específico.

Valores aceptados:
- `BACKLOG`
- `EN_PROGRESO`
- `HECHO`
- `ARCHIVADO`

### `PUT /tareas/?tarea_id=1`

Actualiza la tarea con el ID especificado.

**Body (JSON):**
```json
{
  "titulo": "Diseño final",
  "descripcion": "Actualizar detalles gráficos",
  "estado": "HECHO",
  "prioridad": "BAJA"
}
```

### `DELETE /tareas/?tarea_id=1`

Elimina la tarea con el ID especificado.

