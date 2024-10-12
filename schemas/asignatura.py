from pydantic import BaseModel
from typing import Optional

class AsignaturaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    profesor_id: Optional[int] = None

class AsignaturaCreate(AsignaturaBase):
    pass

class AsignaturaUpdate(AsignaturaBase):
    pass

class Asignatura(AsignaturaBase):
    asignatura_id: int

    class Config:
        orm_mode = True
