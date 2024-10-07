from empleado import Empleado

class Empresa:
    
    def __init__(self, nombre):
        self._nombre = nombre
        self.empleados = []
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def obtener_empleados_empresa(self):
        return len(self.empleados)
        
    def obtener_numero_empleados_departamento(self, departamento):
        contador = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador += 1
        return contador