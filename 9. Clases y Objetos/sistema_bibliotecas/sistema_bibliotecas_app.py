from libro import Libro
from biblioteca import Biblioteca

print('\n***SISTEMA DE BIBLIOTECAS***')

biblioteca1 = Biblioteca('Biblioteca Alejandro')
print(f'\n{biblioteca1.nombre} ha sido creada')

libro1 = Libro('Titulo1', 'Alejandro Romero', 'Programación')
libro2 = Libro('Titulo2', 'Marta García', 'Educativo')
libro3 = Libro('Titulo3', 'Alejandro Romero', 'Programación')
libro4 = Libro('Titulo4', 'Alice Kellen', 'Amoroso')

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)
biblioteca1.agregar_libro(libro4)

biblioteca1.buscar_libro_autor('Marta García')
biblioteca1.buscar_libro_genero('Programación')

biblioteca1.mostrar_todos_libros()

biblioteca1.informacion_libro(libro4)