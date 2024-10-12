from sqlalchemy.orm import Session
from models.asistencia import Asistencia
from schemas.asistencia import AsistenciaCreate, AsistenciaUpdate

def create_asistencia(db: Session, asistencia: AsistenciaCreate):
    db_asistencia = Asistencia(
        estudiante_id=asistencia.estudiante_id,
        fecha=asistencia.fecha,
        estado=asistencia.estado
    )
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

def get_asistencia(db: Session, asistencia_id: int):
    return db.query(Asistencia).filter(Asistencia.asistencia_id == asistencia_id).first()

def get_asistencias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Asistencia).offset(skip).limit(limit).all()

def update_asistencia(db: Session, asistencia_id: int, asistencia: AsistenciaUpdate):
    db_asistencia = db.query(Asistencia).filter(Asistencia.asistencia_id == asistencia_id).first()
    if db_asistencia:
        db_asistencia.estudiante_id = asistencia.estudiante_id
        db_asistencia.fecha = asistencia.fecha
        db_asistencia.estado = asistencia.estado
        db.commit()
        db.refresh(db_asistencia)
    return db_asistencia

def delete_asistencia(db: Session, asistencia_id: int):
    db_asistencia = db.query(Asistencia).filter(Asistencia.asistencia_id == asistencia_id).first()
    if db_asistencia:
        db.delete(db_asistencia)
        db.commit()
    return db_asistencia
