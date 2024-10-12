from sqlalchemy import Column, Integer, Date, String, ForeignKey
from database.db_config import Base
from sqlalchemy.orm import relationship

class Estudiante(Base):
    __tablename__ = 'Estudiantes'

    estudiante_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('Usuarios.usuario_id', ondelete='CASCADE'), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    curso = Column(String(50), nullable=False)

    # Relaciones
    usuario = relationship("Usuario", back_populates="estudiantes")
    notas = relationship("Nota", back_populates="estudiante")
    asistencias = relationship("Asistencia", back_populates="estudiante")
    reportes = relationship("Reporte", back_populates="estudiante")