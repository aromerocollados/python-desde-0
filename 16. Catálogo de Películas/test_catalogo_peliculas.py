from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula

salir = False

while not salir:
    print('''
        1. Agregar película
        2. Listar películas
        3. Eliminar película
        4. Eliminar archivo 
        5. Salir''')

    try:
        opcion = int(input('\nIntroduce una opción (1/5): '))
        
        if opcion < 1 or opcion > 5:
            print('Opción no válida') 
        else:
            if opcion == 1:
                nombre_pelicula = input('Introduce el nombre de la película: ')
                pelicula = Pelicula(nombre_pelicula)
                CatalogoPeliculas.agregar_pelicula(pelicula)
                print('\n--Película añadida')
                
            if opcion == 2:
                CatalogoPeliculas.listar_peliculas()
                
            if opcion == 3:
                nombre_pelicula = input('Introduce el nombre de la película que desea borrar: ')
                CatalogoPeliculas.eliminar_pelicula(nombre_pelicula)
                
            if opcion == 4:
                CatalogoPeliculas.eliminar_peliculas()
                
            if opcion == 5:
                print('\nHasta la próxima...')
                salir = True
    except ValueError:
        print(f'\nOpción no válida: No se permite cadena de texto')