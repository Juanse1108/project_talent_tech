from sqlalchemy import Column, Integer, Enum, DECIMAL, Date, Text, ForeignKey
from database.db_config import Base
from sqlalchemy.orm import relationship

class Nota(Base):
    __tablename__ = 'Notas'

    nota_id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('Estudiantes.estudiante_id', ondelete='CASCADE'), nullable=False)
    asignatura_id = Column(Integer, ForeignKey('Asignaturas.asignatura_id', ondelete='CASCADE'), nullable=False)
    tipo = Column(Enum('examen', 'tarea', 'proyecto'), nullable=False)
    valor = Column(DECIMAL(5, 2), nullable=False)
    fecha = Column(Date)
    comentarios = Column(Text)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="notas")
    asignatura = relationship("Asignatura", back_populates="notas")
