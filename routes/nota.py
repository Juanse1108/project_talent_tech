from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db
from controller.nota import (
    create_nota, get_nota, get_notas, update_nota, delete_nota
)
from schemas.nota import NotaCreate, NotaUpdate, Nota

router = APIRouter()

@router.post("/notas/", response_model=Nota, tags=['Nota'])
def create_nota_endpoint(nota: NotaCreate, db: Session = Depends(get_db)):
    return create_nota(db=db, nota=nota)

@router.get("/notas/{nota_id}", response_model=Nota, tags=['Nota'])
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = get_nota(db, nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return db_nota

@router.get("/notas/", response_model=list[Nota], tags=['Nota'])
def read_notas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_notas(db, skip=skip, limit=limit)

@router.put("/notas/{nota_id}", response_model=Nota, tags=['Nota'])
def update_nota_endpoint(nota_id: int, nota: NotaUpdate, db: Session = Depends(get_db)):
    db_nota = update_nota(db=db, nota_id=nota_id, nota=nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return db_nota

@router.delete("/notas/{nota_id}", response_model=Nota, tags=['Nota'])
def delete_nota_endpoint(nota_id: int, db: Session = Depends(get_db)):
    db_nota = delete_nota(db=db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return db_nota
