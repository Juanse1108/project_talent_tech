from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database.db_config import Base
from sqlalchemy.orm import relationship

class Asignatura(Base):
    __tablename__ = 'Asignaturas'

    asignatura_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    profesor_id = Column(Integer, ForeignKey('Usuarios.usuario_id'))

    # Relaciones
    profesor = relationship("Usuario", back_populates="asignaturas")