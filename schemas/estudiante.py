from pydantic import BaseModel
from datetime import date

class EstudianteBase(BaseModel):
    usuario_id: int
    fecha_nacimiento: date
    curso: str

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    estudiante_id: int

    class Config:
        orm_mode = True
