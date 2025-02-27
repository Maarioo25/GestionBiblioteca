# Mario Bueno López 2ºDAM

from biblioteca.biblioteca import Biblioteca
from biblioteca.menu import Menu
from database import Base, engine

def main():

# Por si necesitas meter datos, pero deberían de estar ya dentro de la base de datos.
    # libros = [
    #     ("9788437604947", "Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", None, 
    #     "Sigue la historia de la familia Buendía en Macondo.", 5),
        
    #     ("9780140449266", "Crimen y castigo", "Fiódor Dostoyevski", "Novela", None, 
    #     "Explora la mente atormentada de un joven estudiante tras cometer un crimen.", 3),

    #     ("9788499890944", "1984", "George Orwell", "Distopía", None, 
    #     "Una sociedad totalitaria bajo la vigilancia constante del Gran Hermano.", 4),

    #     ("9788466350353", "El principito", "Antoine de Saint-Exupéry", "Fábula", None, 
    #     "Un piloto perdido en el desierto conoce a un pequeño príncipe de otro planeta.", 6),

    #     ("9788420674209", "Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", None, 
    #     "Las aventuras de un hidalgo que cree ser un caballero andante.", 2)
    # ]

    # usuarios = [
    #     ("12345678A", "Juan Pérez", "juan.perez@email.com", "600123456", "Calle Falsa 123"),
    #     ("87654321B", "María López", "maria.lopez@email.com", "611987654", "Avenida Siempre Viva 742"),
    #     ("11223344C", "Carlos García", "carlos.garcia@email.com", "622334455", "Plaza Mayor 10"),
    #     ("44332211D", "Laura Fernández", "laura.fernandez@email.com", "633445566", "Calle Luna 15"),
    #     ("55667788E", "David Martínez", "david.martinez@email.com", "644556677", "Paseo del Prado 22")
    # ]

    

    biblioteca = Biblioteca()
    Base.metadata.create_all(bind=engine)
    menu = Menu(biblioteca)
    # for dni, nombre, email, telefono, domicilio in usuarios:
    #     biblioteca.alta_usuario(dni, nombre, email, telefono, domicilio)

    # for isbn, titulo, autor, genero, portada, sinopsis, ejemplares in libros:
    #     biblioteca.alta_libro(isbn, titulo, autor, genero, portada, sinopsis, ejemplares)
    menu.mostrar_menu()

if __name__ == "__main__":
    main()