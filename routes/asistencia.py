from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db
from controller.asistencia import (
    create_asistencia, get_asistencia, get_asistencias, update_asistencia, delete_asistencia
)
from schemas.asistencia import AsistenciaCreate, AsistenciaUpdate, Asistencia

router = APIRouter()

@router.post("/asistencias/", response_model=Asistencia, tags=['Asistencia'])
def create_asistencia_endpoint(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    return create_asistencia(db=db, asistencia=asistencia)

@router.get("/asistencias/{asistencia_id}", response_model=Asistencia, tags=['Asistencia'])
def read_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    db_asistencia = get_asistencia(db, asistencia_id)
    if db_asistencia is None:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return db_asistencia

@router.get("/asistencias/", response_model=list[Asistencia], tags=['Asistencia'])
def read_asistencias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_asistencias(db, skip=skip, limit=limit)

@router.put("/asistencias/{asistencia_id}", response_model=Asistencia, tags=['Asistencia'])
def update_asistencia_endpoint(asistencia_id: int, asistencia: AsistenciaUpdate, db: Session = Depends(get_db)):
    db_asistencia = update_asistencia(db=db, asistencia_id=asistencia_id, asistencia=asistencia)
    if db_asistencia is None:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return db_asistencia

@router.delete("/asistencias/{asistencia_id}", response_model=Asistencia, tags=['Asistencia'])
def delete_asistencia_endpoint(asistencia_id: int, db: Session = Depends(get_db)):
    db_asistencia = delete_asistencia(db=db, asistencia_id=asistencia_id)
    if db_asistencia is None:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return db_asistencia
