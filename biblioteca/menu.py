# Mario Bueno López 2ºDAM

class Menu:
    
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.ejecutando = True
    
    def mostrar_menu(self):
        while self.ejecutando:
            print("\n")
            print("------------------------------------------------")
            print("        SISTEMA DE GESTIÓN DE BIBLIOTECA        ")
            print("------------------------------------------------")
            
            print("1. Alta de socio")
            print("2. Baja de socio")
            print("3. Alta de libro")
            print("4. Baja de libro")
            print("5. Prestar libro")
            print("6. Devolver libro")
            print("7. Consultar libros")
            print("8. Consultar usuarios")
            print("9. Consultar préstamos")
            print("0. Salir")
            print("")
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                self.alta_usuario()
            elif opcion == "2":
                self.baja_usuario()
            elif opcion == "3":
                self.alta_libro()
            elif opcion == "4":
                self.baja_libro()
            elif opcion == "5":
                self.prestar_libro()
            elif opcion == "6":
                self.devolver_libro()
            elif opcion == "7":
                self.consultar_libros()
            elif opcion == "8":
                self.consultar_usuarios()
            elif opcion == "9":
                self.consultar_prestamos()
            elif opcion == "0":
                self.salir()
            else:
                print("\n¡Opción no válida!")

            
    def alta_usuario(self):
        print("\n")
        print("--- ALTA DE USUARIO ---")
        dni = input("DNI: ")
        nombre = input("Nombre completo: ")
        email = input("Correo electrónico: ")
        telefono = input("Teléfono: ")
        domicilio = input("Domicilio: ")
        
        if self.biblioteca.alta_usuario(dni, nombre, email, telefono, domicilio):
            print("Usuario registrado.")
        else:
            print("Ya existe el usuario")
            
    def baja_usuario(self):
        print("\n")
        print("--- BAJA DE USUARIO ---")
        dni = input("DNI del usuario: ")
        
        if self.biblioteca.baja_usuario(dni):
            print("Usuario eliminado.")
        else:
            usuario = self.biblioteca.buscar_usuario(dni)
            if usuario:
                print("El usuario tiene préstamos pendientes.")
            else:
                print("No existe un usuario con ese DNI.")
            
    def alta_libro(self):
        print("\n")
        print("--- ALTA DE LIBRO ---")
        isbn = input("ISBN: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        portada = input("Portada (ruta a la imagen): ")
        sinopsis = input("Sinopsis: ")
        ejemplares = int(input("Número de ejemplares: "))
        
        if self.biblioteca.alta_libro(isbn, titulo, autor, genero, portada, sinopsis, ejemplares):
            print("Libro registrado correctamente.")
        else:
            print("Ya existe un libro con ese ISBN.")
            
    def baja_libro(self):
        print("\n")
        print("--- BAJA DE LIBRO ---")
        isbn = input("ISBN del libro a dar de baja: ")
    
        if self.biblioteca.baja_libro(isbn):
            print("Libro eliminado.")
        else:
            print("El libro tiene préstamos o no existe.")
            
    def prestar_libro(self):
        print("\n")
        print("--- PRÉSTAMO DE LIBRO ---")
        isbn = input("ISBN del libro: ")
        dni = input("DNI del usuario: ")
    
        if self.biblioteca.prestar_libro(isbn, dni):
            print("Préstamo hecho.")
        else:
            print("El libro o el usuario no existen o no hay ejemplares.")
            
    def devolver_libro(self):
        print("\n")
        print("--- DEVOLUCIÓN DE LIBRO ---")
        isbn = input("ISBN del libro: ")
        dni = input("DNI del usuario: ")
    
        if self.biblioteca.devolver_libro(isbn, dni):
            print("Devolución hecha.")
        else:
            print("Error: libro, usuario o préstamo no existen.")
            
    def consultar_libros(self):
        print("\n")
        print("--- LISTADO DE LIBROS ---")
    
        libros = self.biblioteca.listar_libros()
    
        if not libros:
            print("No hay libros registrados.")
        else:
            for i, libro in enumerate(libros, 1):
                print(f"{i}. {libro}")

        input("\nPresiona Enter para continuar...")
            
    def consultar_usuarios(self):
        print("\n")
        print("--- LISTADO DE USUARIOS ---")

        usuarios = self.biblioteca.listar_usuarios()

        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            for i, usuario in enumerate(usuarios, 1):
                print(f"{i}. {usuario}")
                
                if usuario.libros_prestados:
                    libros_prestados = usuario.libros_prestados.split(",")
                    print("  Libros en préstamo:")
                    
                    for isbn in libros_prestados:
                        libro = self.biblioteca.buscar_libro(isbn.strip())
                        if libro:
                            print(f"  - {libro.titulo} ({libro.isbn})")

        input("\nPresiona Enter para continuar...")


    def consultar_prestamos(self):
        print("\n")
        print("--- LISTADO DE PRÉSTAMOS ---")

        prestamos = self.biblioteca.listar_prestamos()

        if not prestamos:
            print("No hay préstamos registrados.")
        else:
            for i, prestamo in enumerate(prestamos, 1):
                print(f"{i}. {prestamo}")

        input("\nPresiona Enter para continuar...")
    
    def salir(self):
        print("Saliendo del programa")
        self.ejecutando = False