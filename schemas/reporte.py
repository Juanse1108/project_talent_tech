from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReporteBase(BaseModel):
    estudiante_id: int
    fecha_generacion: date
    contenido: str

class ReporteCreate(ReporteBase):
    pass

class ReporteUpdate(ReporteBase):
    pass

class Reporte(ReporteBase):
    reporte_id: int

    class Config:
        orm_mode = True
