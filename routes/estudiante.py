from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db
from controller.estudiante import (
    create_estudiante, get_estudiante, get_estudiantes, update_estudiante, delete_estudiante
)
from schemas.estudiante import EstudianteCreate, EstudianteUpdate, Estudiante

router = APIRouter()

@router.post("/estudiantes/", response_model=Estudiante, tags=['Estudiante'])
def create_estudiante_endpoint(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    return create_estudiante(db=db, estudiante=estudiante)

@router.get("/estudiantes/{estudiante_id}", response_model=Estudiante, tags=['Estudiante'])
def read_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = get_estudiante(db, estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante

@router.get("/estudiantes/", response_model=list[Estudiante], tags=['Estudiante'])
def read_estudiantes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_estudiantes(db, skip=skip, limit=limit)

@router.put("/estudiantes/{estudiante_id}", response_model=Estudiante, tags=['Estudiante'])
def update_estudiante_endpoint(estudiante_id: int, estudiante: EstudianteUpdate, db: Session = Depends(get_db)):
    db_estudiante = update_estudiante(db=db, estudiante_id=estudiante_id, estudiante=estudiante)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante

@router.delete("/estudiantes/{estudiante_id}", response_model=Estudiante, tags=['Estudiante'])
def delete_estudiante_endpoint(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = delete_estudiante(db=db, estudiante_id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante
