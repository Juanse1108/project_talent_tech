from pydantic import BaseModel
from datetime import date
from typing import Optional

class AsistenciaBase(BaseModel):
    estudiante_id: int
    fecha: date
    estado: str

class AsistenciaCreate(AsistenciaBase):
    pass

class AsistenciaUpdate(AsistenciaBase):
    pass

class Asistencia(AsistenciaBase):
    asistencia_id: int

    class Config:
        orm_mode = True
