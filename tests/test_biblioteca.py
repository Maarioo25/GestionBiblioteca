# Mario Bueno López 2ºDAM

import pytest
from datetime import datetime
from unittest.mock import MagicMock
from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.prestamo import Prestamo
from biblioteca.usuario import Usuario

@pytest.fixture
def biblioteca():
    biblioteca = Biblioteca()
    biblioteca.db = MagicMock()
    return biblioteca

def test_alta_usuario_exitoso(biblioteca):
    biblioteca.buscar_usuario = MagicMock(return_value=None)
    
    assert biblioteca.alta_usuario("12345678A", "Juan Pérez", "juan@example.com", "600123456", "Calle 1")
    biblioteca.db.add.assert_called()
    biblioteca.db.commit.assert_called()

def test_alta_usuario_existente(biblioteca):
    biblioteca.buscar_usuario = MagicMock(return_value=Usuario(dni="12345678A"))
    
    assert not biblioteca.alta_usuario("12345678A", "Juan Pérez", "juan@example.com", "600123456", "Calle 1")

def test_baja_usuario_exitoso(biblioteca):
    usuario = Usuario(dni="12345678A")
    biblioteca.buscar_usuario = MagicMock(return_value=usuario)

    assert biblioteca.baja_usuario("12345678A")
    biblioteca.db.delete.assert_called_with(usuario)
    biblioteca.db.commit.assert_called()

def test_baja_usuario_inexistente(biblioteca):
    biblioteca.buscar_usuario = MagicMock(return_value=None)
    
    assert not biblioteca.baja_usuario("12345678A")

def test_buscar_usuario(biblioteca):
    usuario = Usuario(dni="12345678A")
    biblioteca.db.query().filter().first.return_value = usuario

    assert biblioteca.buscar_usuario("12345678A") == usuario

def test_alta_libro_exitoso(biblioteca):
    biblioteca.buscar_libro = MagicMock(return_value=None)

    assert biblioteca.alta_libro("978-1234567890", "Libro Ejemplo", "Autor", "Ficción", "imagen.jpg", "Sinopsis", 5)
    biblioteca.db.add.assert_called()
    biblioteca.db.commit.assert_called()

def test_alta_libro_existente(biblioteca):
    biblioteca.buscar_libro = MagicMock(return_value=Libro(isbn="978-1234567890"))

    assert not biblioteca.alta_libro("978-1234567890", "Libro Ejemplo", "Autor", "Ficción", "imagen.jpg", "Sinopsis", 5)

def test_baja_libro_exitoso(biblioteca):
    libro = Libro(isbn="978-1234567890")
    biblioteca.buscar_libro = MagicMock(return_value=libro)

    assert biblioteca.baja_libro("978-1234567890")
    biblioteca.db.delete.assert_called_with(libro)
    biblioteca.db.commit.assert_called()

def test_baja_libro_inexistente(biblioteca):
    biblioteca.buscar_libro = MagicMock(return_value=None)

    assert not biblioteca.baja_libro("978-1234567890")

def test_buscar_libro(biblioteca):
    libro = Libro(isbn="978-1234567890")
    biblioteca.db.query().filter().first.return_value = libro

    assert biblioteca.buscar_libro("978-1234567890") == libro

def test_prestar_libro_exitoso(biblioteca):
    libro = Libro(isbn="978-1234567890", ejemplares_disponibles=3)
    usuario = Usuario(dni="12345678A", libros_prestados=None)
    
    biblioteca.buscar_libro = MagicMock(return_value=libro)
    biblioteca.buscar_usuario = MagicMock(return_value=usuario)

    assert biblioteca.prestar_libro("978-1234567890", "12345678A")
    assert libro.ejemplares_disponibles == 2
    biblioteca.db.add.assert_called()
    biblioteca.db.commit.assert_called()

def test_prestar_libro_sin_ejemplares(biblioteca):
    libro = Libro(isbn="978-1234567890", ejemplares_disponibles=0)
    usuario = Usuario(dni="12345678A")

    biblioteca.buscar_libro = MagicMock(return_value=libro)
    biblioteca.buscar_usuario = MagicMock(return_value=usuario)

    assert not biblioteca.prestar_libro("978-1234567890", "12345678A")

def test_prestar_libro_usuario_inexistente(biblioteca):
    libro = Libro(isbn="978-1234567890", ejemplares_disponibles=3)
    biblioteca.buscar_libro = MagicMock(return_value=libro)
    biblioteca.buscar_usuario = MagicMock(return_value=None)

    assert not biblioteca.prestar_libro("978-1234567890", "12345678A")

def test_devolver_libro_exitoso(biblioteca):
    prestamo = Prestamo(libro_isbn="978-1234567890", usuario_dni="12345678A", devuelto=False)
    libro = Libro(isbn="978-1234567890", ejemplares_disponibles=2)
    usuario = Usuario(dni="12345678A", libros_prestados="978-1234567890")

    biblioteca.db.query().filter().first.side_effect = [prestamo, libro, usuario]

    assert biblioteca.devolver_libro("978-1234567890", "12345678A")
    assert prestamo.devuelto is True
    assert libro.ejemplares_disponibles == 3
    biblioteca.db.commit.assert_called()

def test_devolver_libro_no_prestado(biblioteca):
    biblioteca.db.query().filter().first.return_value = None

    assert not biblioteca.devolver_libro("978-1234567890", "12345678A")

def test_listar_libros(biblioteca):
    biblioteca.db.query().all.return_value = [Libro(isbn="978-1234567890"), Libro(isbn="978-0987654321")]
    
    assert len(biblioteca.listar_libros()) == 2

def test_listar_usuarios(biblioteca):
    biblioteca.db.query().all.return_value = [Usuario(dni="12345678A"), Usuario(dni="87654321B")]

    assert len(biblioteca.listar_usuarios()) == 2

def test_listar_prestamos(biblioteca):
    biblioteca.db.query().all.return_value = [Prestamo(libro_isbn="978-1234567890", usuario_dni="12345678A")]

    assert len(biblioteca.listar_prestamos()) == 1