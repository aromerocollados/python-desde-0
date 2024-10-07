from libro import Libro

class Biblioteca:
    
    def __init__(self, nombre):
        self._nombre = nombre
        self.libros = []
      
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def buscar_libro_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                self.informacion_libro(libro)
                
    def buscar_libro_genero(self, genero):
        for libro in self.libros:
            if libro.genero == genero:
                self.informacion_libro(libro)
                
    def mostrar_todos_libros(self):
        for libro in self.libros:
            self.informacion_libro(libro)
            
    def informacion_libro(self, libro):
        print(f'''
              **INFORMACIÓN DEL LIBRO**
              -------------------------
              - Título: {libro.titulo}
              - Autor: {libro.autor}
              - Género: {libro.genero}''')
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre               