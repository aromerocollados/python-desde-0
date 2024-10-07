class Libro:
    
    def __init__(self, titulo, autor, genero):
      self._titulo = titulo
      self._autor = autor
      self._genero = genero
      
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def genero(self):
        return self._genero
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        
    @autor.setter
    def autor(self, autor):
        self._autor = autor
        
    @genero.setter
    def genero(self, genero):
        self._genero = genero