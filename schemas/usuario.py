from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    rol: str
    contraseña: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    usuario_id: int

    class Config:
        orm_mode = True