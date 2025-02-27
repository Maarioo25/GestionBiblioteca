# Manual de Usuario - Sistema de Gestión de Biblioteca

## Introducción

Este manual proporciona instrucciones detalladas sobre cómo utilizar el Sistema de Gestión de Biblioteca. El sistema permite administrar usuarios, libros y préstamos de una biblioteca a través de la terminal.

## Inicio del Sistema

Para iniciar el sistema, abra una terminal en el directorio del proyecto y ejecute:

```
python main.py
```

## Menú Principal

Al iniciar el sistema, se mostrará el menú principal con las siguientes opciones:

-  1. Alta de socio
-  2. Baja de socio
-  3. Alta de libro
-  4. Baja de libro
-  5. Prestar libro
-  6. Devolver libro
-  7. Consultar libros
-  8. Consultar usuarios
- 9. Consultar préstamos
- 0. Salir

Para seleccionar una opción, introduzca el número correspondiente y presione Enter.

## Gestión de Usuarios

### Alta de Socio

Para registrar un nuevo usuario:

1. Seleccione la opción "1. Alta de socio" en el menú principal.
2. Introduzca los datos solicitados:
   - DNI: identificador único del usuario (por ejemplo, "12345678A")
   - Nombre completo
   - Correo electrónico
   - Teléfono
   - Domicilio

Si el DNI ya existe en el sistema, se mostrará un mensaje de error y no se registrará el usuario.

### Baja de Socio

Para dar de baja a un usuario:

1. Seleccione la opción "2. Baja de socio" en el menú principal.
2. Introduzca el DNI del usuario a dar de baja.

Si el usuario tiene préstamos pendientes, no podrá ser eliminado y se mostrará un mensaje de error.

### Consultar Usuarios

Para ver la lista de usuarios registrados:

1. Seleccione la opción "8. Consultar usuarios" en el menú principal.
2. Se mostrará una lista numerada de todos los usuarios.

## Gestión de Libros

### Alta de Libro

Para registrar un nuevo libro:

1. Seleccione la opción "3. Alta de libro" en el menú principal.
2. Introduzca los datos solicitados:
   - ISBN: identificador único del libro (por ejemplo, "9788401352836")
   - Título
   - Autor
   - Género
   - Ruta de la imagen de portada
   - Sinopsis
   - Número de ejemplares

Si el ISBN ya existe en el sistema, se mostrará un mensaje de error y no se registrará el libro.

### Baja de Libro

Para dar de baja un libro:

1. Seleccione la opción "4. Baja de libro" en el menú principal.
2. Introduzca el ISBN del libro a dar de baja.

Si el libro tiene préstamos pendientes, no podrá ser eliminado y se mostrará un mensaje de error.

### Consultar Libros

Para ver la lista de libros registrados:

1. Seleccione la opción "7. Consultar libros" en el menú principal.
2. Se mostrará una lista numerada de todos los libros.

## Gestión de Préstamos

### Prestar Libro

Para registrar un préstamo:

1. Seleccione la opción "5. Prestar libro" en el menú principal.
2. Introduzca el ISBN del libro a prestar.
3. Introduzca el DNI del usuario que recibirá el préstamo.

Para poder realizar el préstamo:
- El libro y el usuario deben existir en el sistema.
- Debe haber ejemplares disponibles del libro.

### Devolver Libro

Para registrar una devolución:

1. Seleccione la opción "6. Devolver libro" en el menú principal.
2. Introduzca el ISBN del libro a devolver.
3. Introduzca el DNI del usuario que devuelve el libro.

Para poder realizar la devolución, debe existir un préstamo activo para ese libro y usuario.

### Consultar Préstamos

Para ver la lista de préstamos:

1. Seleccione la opción "9. Consultar préstamos" en el menú principal.
2. Se mostrará una lista numerada de los préstamos.

## Salir del Sistema

Para salir del sistema:

1. Seleccione la opción "0. Salir" en el menú principal.
2. Se mostrará un mensaje de despedida y se cerrará la aplicación.

## Consejos y Solución de Problemas

- Asegúrese de introducir correctamente los identificadores (DNI e ISBN) para evitar errores.
- Si un usuario o libro no puede ser eliminado debido a préstamos pendientes, primero registre las devoluciones correspondientes.
- Si comete un error al introducir datos, puede volver al menú principal y volver a intentarlo.

# Mario Bueno López 2ºDAM