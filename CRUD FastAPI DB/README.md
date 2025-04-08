# FastAPI Backend

Un backend RESTful desarrollado con FastAPI para la gestión de usuarios.

## Descripción

Este proyecto es una API REST construida con FastAPI y SQLAlchemy que proporciona endpoints para gestionar información de usuarios. Permite operaciones CRUD completas para entidades de usuario con validación de datos mediante Pydantic.

## Tecnologías utilizadas

- Python 3.9+
- FastAPI 0.95+
- SQLAlchemy 2.0+ (versión asíncrona)
- Pydantic 2.0+
- SQLite (para desarrollo)
- Uvicorn (servidor ASGI)

## Requisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## Estructura del proyecto

```
CRUD FastAPI DB/
├── app/
│   ├── __init__.py
│   ├── main.py             # Punto de entrada de la aplicación
│   ├── crud/               # Operaciones CRUD
│   │   ├── __init__.py
│   │   └── user.py         # Operaciones CRUD para usuarios
│   ├── db/                 # Configuración de la base de datos
│   │   ├── __init__.py
│   │   └── database.py     # Configuración SQLAlchemy
│   ├── models/             # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   └── user.py         # Modelo de usuario
│   └── schemas/            # Esquemas Pydantic
│       ├── __init__.py
│       └── user.py         # Esquemas para validación de datos
├── populate_db.py          # Script para poblar la base de datos
├── test.db                 # Base de datos SQLite
└── README.md               # Este archivo
```

## Instalación

1. Clona este repositorio:

```bash
git clone <url-del-repositorio>
cd "CRUD FastAPI DB"
```

2. Crea un entorno virtual e instala las dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install fastapi sqlalchemy pydantic uvicorn
```

También puedes crear un archivo requirements.txt con:

```
fastapi>=0.95.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
uvicorn>=0.20.0
```

Y luego instalar con:

```bash
pip install -r requirements.txt
```

## Uso

### Iniciar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`.

### API Endpoints

#### Usuarios

- `POST /users/`: Crear un nuevo usuario
- `GET /users/`: Obtener todos los usuarios
- `GET /users/{user_id}`: Obtener un usuario por ID
- `PUT /users/{user_id}`: Actualizar un usuario existente
- `DELETE /users/{user_id}`: Eliminar un usuario

### Documentación de la API

FastAPI genera automáticamente documentación interactiva:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Script para poblar la base de datos

Para cargar datos de prueba en la base de datos, ejecuta:

```bash
python populate_db.py
```
