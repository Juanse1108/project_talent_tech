from sqlalchemy.orm import Session
from models.reporte import Reporte
from schemas.reporte import ReporteCreate, ReporteUpdate

def create_reporte(db: Session, reporte: ReporteCreate):
    db_reporte = Reporte(
        estudiante_id=reporte.estudiante_id,
        fecha_generacion=reporte.fecha_generacion,
        contenido=reporte.contenido
    )
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte

def get_reporte(db: Session, reporte_id: int):
    return db.query(Reporte).filter(Reporte.reporte_id == reporte_id).first()

def get_reportes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reporte).offset(skip).limit(limit).all()

def update_reporte(db: Session, reporte_id: int, reporte: ReporteUpdate):
    db_reporte = db.query(Reporte).filter(Reporte.reporte_id == reporte_id).first()
    if db_reporte:
        db_reporte.estudiante_id = reporte.estudiante_id
        db_reporte.fecha_generacion = reporte.fecha_generacion
        db_reporte.contenido = reporte.contenido
        db.commit()
        db.refresh(db_reporte)
    return db_reporte

def delete_reporte(db: Session, reporte_id: int):
    db_reporte = db.query(Reporte).filter(Reporte.reporte_id == reporte_id).first()
    if db_reporte:
        db.delete(db_reporte)
        db.commit()
    return db_reporte
