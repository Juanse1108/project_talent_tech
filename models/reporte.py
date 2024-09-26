from sqlalchemy import Column, Integer, Date, Text, ForeignKey
from database.db_config import Base
from sqlalchemy.orm import relationship

class Reporte(Base):
    __tablename__ = 'Reportes'

    reporte_id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('Estudiantes.estudiante_id', ondelete="CASCADE"), nullable=False)
    fecha_generacion = Column(Date)
    contenido = Column(Text)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="reportes")
