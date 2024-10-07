import os


class CatalogoPeliculas:
    ruta_archivo = '16. Catálogo de Películas/peliculas.txt'
    
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding = 'utf-8') as archivo:
            archivo.write(pelicula.nombre + '\n')
            
    @classmethod
    def listar_peliculas(cls):
        try: 
            with open(cls.ruta_archivo, 'r', encoding = 'utf-8') as archivo:
                print(f'Catálogo de peliculas'.center(50, '-'))
                print(archivo.read())
        except FileNotFoundError:
            print(f'No se ha encontrado el archivo: {cls.ruta_archivo}')
            
    @classmethod     
    def eliminar_peliculas(cls):
        try: 
            os.remove(cls.ruta_archivo)
            print(f'\nArchivo eliminado: {cls.ruta_archivo}')
        except FileNotFoundError:
            print(f'No se ha encontrado el archivo: {cls.ruta_archivo}')
        
    @classmethod
    def eliminar_pelicula(cls, nombre_pelicula):
        try:
            with open(cls.ruta_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
            
            with open(cls.ruta_archivo, 'w', encoding='utf-8') as archivo:
                for linea in lineas:
                    if linea.strip() != nombre_pelicula:
                        archivo.write(linea)
                    else:
                        print(f'Película eliminada: {nombre_pelicula}')
            
        except FileNotFoundError:
            print(f'No se ha encontrado el archivo: {cls.ruta_archivo}')