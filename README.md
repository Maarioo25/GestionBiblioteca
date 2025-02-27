# Sistema de Gestión de Biblioteca Mario Bueno López 2ºDAM

Aplicación para la gestión de una biblioteca implementada en Python utilizando Programación Orientada a Objetos (POO).

## Características

* Gestión de usuarios (alta, baja, consulta)
* Gestión de libros (alta, baja, consulta)
* Gestión de préstamos (préstamo, devolución, consulta)
* Interfaz de línea de comandos (CLI)

## Requisitos

* Python 3.9 o superior

## Instalación

1. Clona este repositorio:

```
git clone https://github.com/Maarioo25/GestionBiblioteca
cd GestionBiblioteca
```

2. Opcionalmente, crea un entorno virtual:

```
python -m venv venv
venv\Scripts\activate
```

3. Instala las dependencias:

```
pip install -r requirements.txt
```

## Uso

Para iniciar la aplicación, ejecuta:

```
python main.py
```

La aplicación mostrará un menú interactivo con las siguientes opciones:

-   1. Alta de socio
-   2. Baja de socio
-   3. Alta de libro
-   4. Baja de libro
-   5. Prestar libro
-   6. Devolver libro
-   7. Consultar libros
-   8. Consultar usuarios
-   9. Consultar préstamos
-   0. Salir

## Estructura del proyecto

```
Biblioteca/
│
├── biblioteca/             # Paquete principal
│   ├── biblioteca.py       # Clase principal Biblioteca
│   ├── libro.py            # Clase Libro
│   ├── usuario.py          # Clase Usuario
│   ├── prestamo.py         # Clase Prestamo
│   └── menu.py             # Interfaz CLI
├── doc/                    
│   └── documentation.py    # Documentación
├── tests/                    
│   └── test_biblioteca.py  # Tests de la biblioteca
│
├── LICENSE                 # Licencia del programa
├── README.md               # Este archivo
├── requirements.txt        # Dependencias
├── setup.py                # Distribución
├── biblioteca.db           # Base de datos
├── database.py             # Configuración de la base de datos
└── main.py                 # Inicio del programa
```
