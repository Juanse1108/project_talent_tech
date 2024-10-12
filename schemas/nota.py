from pydantic import BaseModel
from datetime import date
from typing import Optional

class NotaBase(BaseModel):
    estudiante_id: int
    asignatura_id: int
    tipo: str
    valor: float
    fecha: Optional[date] = None
    comentarios: Optional[str] = None

class NotaCreate(NotaBase):
    pass

class NotaUpdate(NotaBase):
    pass

class Nota(NotaBase):
    nota_id: int

    class Config:
        orm_mode = True
