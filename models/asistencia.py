from sqlalchemy import Column, Integer, Date, Enum, ForeignKey
from database.db_config import Base
from sqlalchemy.orm import relationship

class Asistencia(Base):
    __tablename__ = 'Asistencia'

    asistencia_id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('Estudiantes.estudiante_id', ondelete="CASCADE"), nullable=False)
    fecha = Column(Date)
    estado = Column(Enum('presente', 'ausente', 'tarde'), nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="asistencias")
