class Empleado:
    
    contador = 0
    
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador += 1
      
    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador