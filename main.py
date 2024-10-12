from fastapi import FastAPI
from database.db_config import engine, Base
from database.db_config import get_db 
from routes import usuario  # Importación absoluta desde el módulo 'routes'
from routes import asignatura  # Importación absoluta desde el módulo 'routes'
from routes import estudiante  # Importación absoluta desde el módulo 'routes'
from routes import nota  # Importación absoluta desde el módulo 'routes'
from routes import asistencia  # Importación absoluta desde el módulo 'routes'
from routes import reporte  # Importación absoluta desde el módulo 'routes'

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()
app.title = "Colegio - Proyecto Talent Tech" #asigna un valor al atributo title
app.version = "0.0.1"

# Incluir el router de 'usuario'
app.include_router(usuario.router)
app.include_router(asignatura.router)
app.include_router(estudiante.router)
app.include_router(nota.router)
app.include_router(asistencia.router)
app.include_router(reporte.router)
