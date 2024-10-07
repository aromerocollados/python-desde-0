class Persona:
    
    contador = 0
    
    def __init__(self, nombre, edad = 0):
        self._nombre = nombre
        self._edad = edad
        Persona.contador += 1
        
    def imprimir_persona(self):
        print(f'\nNombre: {self.nombre} \nEdad: {self.edad}')
 
    @staticmethod # Método estático
    def contador_personas():
        return Persona.contador
    
    @classmethod # Más pythonico
    def contador_personas_clase(cls):
        return cls.contador
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
if __name__ == '__main__':
    persona1 = Persona('Alejandro')
    persona1.edad = 21
    persona1.imprimir_persona()
    
    persona2 = Persona('Paula', 19)
    persona2.imprimir_persona()
    
    print(f'\nLa cantidad de personas añadidas es de {Persona.contador}')
    print(f'\nLa cantidad de personas añadidas es de {Persona.contador_personas()} (Método estático)')
    print(f'\nLa cantidad de personas añadidas es de {Persona.contador_personas_clase()} (Método clase)')
    