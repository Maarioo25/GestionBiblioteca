# Mario Bueno López 2ºDAM

from sqlalchemy import Column, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    dni = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    telefono = Column(String, nullable=False)
    domicilio = Column(String, nullable=False)
    libros_prestados = Column(String, nullable=True)

    def __repr__(self):
        num_libros_prestados = len(self.libros_prestados.split(",")) if self.libros_prestados else 0
        return (
            f"< Usuario ("
            f"DNI = '{self.dni}', "
            f"Nombre = '{self.nombre}', "
            f"Email = '{self.email}', "
            f"Teléfono = '{self.telefono}', "
            f"Domicilio = '{self.domicilio}', "
            f"Libros Prestados = {num_libros_prestados} "
            f")>"
        )
