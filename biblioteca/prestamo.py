# Mario Bueno López 2ºDAM

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from database import Base

class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    libro_isbn = Column(String, ForeignKey("libros.isbn"))
    usuario_dni = Column(String, ForeignKey("usuarios.dni"))
    fecha_prestamo = Column(DateTime, default=datetime.utcnow)
    fecha_devolucion = Column(DateTime, nullable=True)
    devuelto = Column(Boolean, default=False)

    def __repr__(self):
        estado = "Devuelto" if self.devuelto else "No devuelto"
        fecha_prestamo_str = self.fecha_prestamo.strftime("%Y-%m-%d %H:%M:%S")
        fecha_devolucion_str = (
            self.fecha_devolucion.strftime("%Y-%m-%d %H:%M:%S")
            if self.fecha_devolucion
            else "Por Determinar"
        )

        return (
            f"<Préstamo ( ID = {self.id}, "
            f"Libro ISBN = '{self.libro_isbn}', "
            f"DNI Usuario = '{self.usuario_dni}', "
            f"Fecha Préstamo = '{fecha_prestamo_str}', "
            f"Fecha Devolución = '{fecha_devolucion_str}', "
            f"Estado = '{estado}' )>"
        )
