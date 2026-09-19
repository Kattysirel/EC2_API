# API Biblioteca Digital

API RESTful hecha con FastAPI y SQLModel. Permite gestionar libros y préstamos con operaciones CRUD completas.

## Estructura del proyecto

- backend/src/main.py: archivo principal, crea la app de FastAPI y registra los routers. Por sí solo no expone nada, porque solo define la aplicación, no un servidor. Necesita correrse con uvicorn o fastapi run para levantar el puerto.
- backend/src/database/database.py: conexión a la base de datos SQLite y creación de tablas.
- backend/src/models: modelos de SQLModel, representan las tablas Libro y Prestamo.
- backend/src/schemas: esquemas de Pydantic para validar los datos de entrada y salida de cada entidad.
- backend/src/crud: funciones que hacen las operaciones directas contra la base de datos.
- backend/src/routers: endpoints de la API, libro_router.py expone /libros y prestamo_router.py expone /prestamos, cada uno con sus 5 operaciones CRUD.
- backend/requirements.txt: dependencias del proyecto, fastapi[standard] y sqlmodel.

## Cómo ejecutar localmente

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd src
fastapi run main.py

## Documentación

Con la API corriendo, la documentación interactiva está disponible en /docs.

## Despliegue

La API está desplegada en una instancia EC2 de AWS, corriendo con pm2 para mantenerse activa en segundo plano.
