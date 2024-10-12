from sqlalchemy.orm import Session
from models.nota import Nota
from schemas.nota import NotaCreate, NotaUpdate

def create_nota(db: Session, nota: NotaCreate):
    db_nota = Nota(
        estudiante_id=nota.estudiante_id,
        asignatura_id=nota.asignatura_id,
        tipo=nota.tipo,
        valor=nota.valor,
        fecha=nota.fecha,
        comentarios=nota.comentarios
    )
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return db_nota

def get_nota(db: Session, nota_id: int):
    return db.query(Nota).filter(Nota.nota_id == nota_id).first()

def get_notas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Nota).offset(skip).limit(limit).all()

def update_nota(db: Session, nota_id: int, nota: NotaUpdate):
    db_nota = db.query(Nota).filter(Nota.nota_id == nota_id).first()
    if db_nota:
        db_nota.estudiante_id = nota.estudiante_id
        db_nota.asignatura_id = nota.asignatura_id
        db_nota.tipo = nota.tipo
        db_nota.valor = nota.valor
        db_nota.fecha = nota.fecha
        db_nota.comentarios = nota.comentarios
        db.commit()
        db.refresh(db_nota)
    return db_nota

def delete_nota(db: Session, nota_id: int):
    db_nota = db.query(Nota).filter(Nota.nota_id == nota_id).first()
    if db_nota:
        db.delete(db_nota)
        db.commit()
    return db_nota
