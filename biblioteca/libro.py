# Mario Bueno López 2ºDAM

from sqlalchemy import Column, String, Integer
from database import Base

class Libro(Base):
    __tablename__ = "libros"

    isbn = Column(String, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    portada = Column(String, nullable=True)
    sinopsis = Column(String, nullable=False)
    ejemplares = Column(Integer, nullable=False)
    ejemplares_disponibles = Column(Integer, nullable=False)

    def __repr__(self):
        return (
            f"<Libro ( "
            f" ISBN = '{self.isbn}', "
            f"Título = '{self.titulo}', "
            f"Autor = '{self.autor}', "
            f"Género = '{self.genero}'"
            f" )>"
        )

