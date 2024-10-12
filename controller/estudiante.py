from sqlalchemy.orm import Session
from models.estudiante import Estudiante
from schemas.estudiante import EstudianteCreate, EstudianteUpdate

def create_estudiante(db: Session, estudiante: EstudianteCreate):
    db_estudiante = Estudiante(
        usuario_id=estudiante.usuario_id,
        fecha_nacimiento=estudiante.fecha_nacimiento,
        curso=estudiante.curso
    )
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def get_estudiante(db: Session, estudiante_id: int):
    return db.query(Estudiante).filter(Estudiante.estudiante_id == estudiante_id).first()

def get_estudiantes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Estudiante).offset(skip).limit(limit).all()

def update_estudiante(db: Session, estudiante_id: int, estudiante: EstudianteUpdate):
    db_estudiante = db.query(Estudiante).filter(Estudiante.estudiante_id == estudiante_id).first()
    if db_estudiante:
        db_estudiante.usuario_id = estudiante.usuario_id
        db_estudiante.fecha_nacimiento = estudiante.fecha_nacimiento
        db_estudiante.curso = estudiante.curso
        db.commit()
        db.refresh(db_estudiante)
    return db_estudiante

def delete_estudiante(db: Session, estudiante_id: int):
    db_estudiante = db.query(Estudiante).filter(Estudiante.estudiante_id == estudiante_id).first()
    if db_estudiante:
        db.delete(db_estudiante)
        db.commit()
    return db_estudiante
