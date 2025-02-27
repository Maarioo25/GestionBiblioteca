# Mario Bueno López 2ºDAM

from biblioteca.libro import Libro
from biblioteca.prestamo import Prestamo
from biblioteca.usuario import Usuario
from database import SessionLocal

from datetime import datetime

class Biblioteca:
    
    def __init__(self):
        self.db = SessionLocal()

    def alta_usuario(self, dni, nombre, email, telefono, domicilio):
        if self.buscar_usuario(dni):
            return False
        
        nuevo_usuario = Usuario(dni=dni, nombre=nombre, email=email, telefono=telefono, domicilio=domicilio)
        self.db.add(nuevo_usuario)
        self.db.commit()
        return True
    
    def baja_usuario(self, dni):
        usuario = self.buscar_usuario(dni)
        if not usuario:
            return False
    
        self.db.delete(usuario)
        self.db.commit()
        return True

    def buscar_usuario(self, dni):
        return self.db.query(Usuario).filter(Usuario.dni == dni).first()

    def alta_libro(self, isbn, titulo, autor, genero, portada, sinopsis, ejemplares):
        if self.buscar_libro(isbn):
            return False
        
        nuevo_libro = Libro(isbn=isbn, titulo=titulo, autor=autor, genero=genero,
                            portada=portada, sinopsis=sinopsis, ejemplares=ejemplares, ejemplares_disponibles=ejemplares)
        self.db.add(nuevo_libro)
        self.db.commit()
        return True
    
    def baja_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if not libro:
            return False
    
        self.db.delete(libro)
        self.db.commit()
        return True

    def buscar_libro(self, isbn):
        return self.db.query(Libro).filter(Libro.isbn == isbn).first()

    def prestar_libro(self, isbn, dni):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(dni)

        if not libro or not usuario or libro.ejemplares_disponibles <= 0:
            return False

        prestamo = Prestamo(libro_isbn=isbn, usuario_dni=dni, fecha_prestamo=datetime.now(), devuelto=False)
        libro.ejemplares_disponibles -= 1

        if usuario.libros_prestados:
            libros = usuario.libros_prestados.split(",")
            if isbn not in libros:
                libros.append(isbn)
                usuario.libros_prestados = ",".join(libros)
        else:
            usuario.libros_prestados = isbn

        self.db.add(prestamo)
        self.db.commit()
        return True

    def devolver_libro(self, isbn, dni):
        prestamo = self.db.query(Prestamo).filter(
            Prestamo.libro_isbn == isbn,
            Prestamo.usuario_dni == dni,
            Prestamo.devuelto == False
        ).first()

        if not prestamo:
            return False
        
        prestamo.devuelto = True
        prestamo.fecha_devolucion = datetime.now()

        libro = self.buscar_libro(isbn)
        libro.ejemplares_disponibles += 1

        usuario = self.buscar_usuario(dni)
        if usuario.libros_prestados:
            libros = usuario.libros_prestados.split(",")
            if isbn in libros:
                libros.remove(isbn)
                usuario.libros_prestados = ",".join(libros) if libros else None

        self.db.commit()
        return True

    def listar_libros(self):
        return self.db.query(Libro).all()

    def listar_usuarios(self):
        return self.db.query(Usuario).all()

    def listar_prestamos(self):
        return self.db.query(Prestamo).all()
