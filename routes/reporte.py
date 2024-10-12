from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db
from controller.reporte import (
    create_reporte, get_reporte, get_reportes, update_reporte, delete_reporte
)
from schemas.reporte import ReporteCreate, ReporteUpdate, Reporte

router = APIRouter()

@router.post("/reportes/", response_model=Reporte, tags=['Reporte'])
def create_reporte_endpoint(reporte: ReporteCreate, db: Session = Depends(get_db)):
    return create_reporte(db=db, reporte=reporte)

@router.get("/reportes/{reporte_id}", response_model=Reporte, tags=['Reporte'])
def read_reporte(reporte_id: int, db: Session = Depends(get_db)):
    db_reporte = get_reporte(db, reporte_id)
    if db_reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return db_reporte

@router.get("/reportes/", response_model=list[Reporte], tags=['Reporte'])
def read_reportes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_reportes(db, skip=skip, limit=limit)

@router.put("/reportes/{reporte_id}", response_model=Reporte, tags=['Reporte'])
def update_reporte_endpoint(reporte_id: int, reporte: ReporteUpdate, db: Session = Depends(get_db)):
    db_reporte = update_reporte(db=db, reporte_id=reporte_id, reporte=reporte)
    if db_reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return db_reporte

@router.delete("/reportes/{reporte_id}", response_model=Reporte, tags=['Reporte'])
def delete_reporte_endpoint(reporte_id: int, db: Session = Depends(get_db)):
    db_reporte = delete_reporte(db=db, reporte_id=reporte_id)
    if db_reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return db_reporte
