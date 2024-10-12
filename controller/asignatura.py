from sqlalchemy.orm import Session
from models.asignatura import Asignatura
from schemas.asignatura import AsignaturaCreate, AsignaturaUpdate

def create_asignatura(db: Session, asignatura: AsignaturaCreate):
    db_asignatura = Asignatura(
        nombre=asignatura.nombre,
        descripcion=asignatura.descripcion,
        profesor_id=asignatura.profesor_id
    )
    db.add(db_asignatura)
    db.commit()
    db.refresh(db_asignatura)
    return db_asignatura

def get_asignatura(db: Session, asignatura_id: int):
    return db.query(Asignatura).filter(Asignatura.asignatura_id == asignatura_id).first()

def get_asignaturas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Asignatura).offset(skip).limit(limit).all()

def update_asignatura(db: Session, asignatura_id: int, asignatura: AsignaturaUpdate):
    db_asignatura = db.query(Asignatura).filter(Asignatura.asignatura_id == asignatura_id).first()
    if db_asignatura:
        db_asignatura.nombre = asignatura.nombre
        db_asignatura.descripcion = asignatura.descripcion
        db_asignatura.profesor_id = asignatura.profesor_id
        db.commit()
        db.refresh(db_asignatura)
    return db_asignatura

def delete_asignatura(db: Session, asignatura_id: int):
    db_asignatura = db.query(Asignatura).filter(Asignatura.asignatura_id == asignatura_id).first()
    if db_asignatura:
        db.delete(db_asignatura)
        db.commit()
    return db_asignatura
