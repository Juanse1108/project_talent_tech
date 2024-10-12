from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db
from controller.asignatura import (
    create_asignatura, get_asignatura, get_asignaturas, update_asignatura, delete_asignatura
)
from schemas.asignatura import AsignaturaCreate, AsignaturaUpdate, Asignatura

router = APIRouter()

@router.post("/asignaturas/", response_model=Asignatura, tags=['Asignatura'])
def create_asignatura_endpoint(asignatura: AsignaturaCreate, db: Session = Depends(get_db)):
    return create_asignatura(db=db, asignatura=asignatura)

@router.get("/asignaturas/{asignatura_id}", response_model=Asignatura, tags=['Asignatura'])
def read_asignatura(asignatura_id: int, db: Session = Depends(get_db)):
    db_asignatura = get_asignatura(db, asignatura_id)
    if db_asignatura is None:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return db_asignatura

@router.get("/asignaturas/", response_model=list[Asignatura], tags=['Asignatura'])
def read_asignaturas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_asignaturas(db, skip=skip, limit=limit)

@router.put("/asignaturas/{asignatura_id}", response_model=Asignatura, tags=['Asignatura'])
def update_asignatura_endpoint(asignatura_id: int, asignatura: AsignaturaUpdate, db: Session = Depends(get_db)):
    db_asignatura = update_asignatura(db=db, asignatura_id=asignatura_id, asignatura=asignatura)
    if db_asignatura is None:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return db_asignatura

@router.delete("/asignaturas/{asignatura_id}", response_model=Asignatura, tags=['Asignatura'])
def delete_asignatura_endpoint(asignatura_id: int, db: Session = Depends(get_db)):
    db_asignatura = delete_asignatura(db=db, asignatura_id=asignatura_id)
    if db_asignatura is None:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return db_asignatura
