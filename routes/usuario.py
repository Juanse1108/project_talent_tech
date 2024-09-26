from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db # Cambiar a importación absoluta
from controller.usuario import (
    create_usuario, get_usuario, get_usuarios, update_usuario, delete_usuario
) # Cambiar a importación absoluta
from schemas.usuario import UsuarioCreate, UsuarioUpdate, Usuario  # Cambiar a importación absoluta

router = APIRouter()

@router.post("/usuarios/", response_model=Usuario, tags=['Usuario'])
def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db=db, usuario=usuario)

@router.get("/usuarios/{usuario_id}", response_model=Usuario, tags=['Usuario'])
def read_user(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.get("/usuarios/", response_model=list[Usuario], tags=['Usuario'])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.put("/usuarios/{usuario_id}", response_model=Usuario, tags=['Usuario'])
def update_user(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.delete("/usuarios/{usuario_id}", response_model=Usuario, tags=['Usuario'])
def delete_user(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = delete_usuario(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario
