from sqlalchemy import Column, Integer, String, Enum
from database.db_config import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'Usuarios'

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    rol = Column(Enum('estudiante', 'profesor', 'padre'), nullable=False)
    contraseña = Column(String(255), nullable=False)

    # Relaciones
    asignaturas = relationship("Asignatura", back_populates="profesor")
    estudiantes = relationship("Estudiante", back_populates="usuario")