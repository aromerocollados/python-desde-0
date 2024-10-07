from empleado import Empleado
from empresa import Empresa

print('\n***SISTEMA DE EMPLEADOS***')

# Creación de la empresa
empresa1 = Empresa('Anelis Network')
print(f'La empresa {empresa1.nombre} ha sido creada')

# Creación de los empleados
empleado1 = Empleado('Alejandro Romero', 'Informática')
empleado2 = Empleado('Marta García', 'Recursos Humanos')
empleado3 = Empleado('Tomás Primo', 'Informática')

# Contratación de los empleados a la empresa
empresa1.contratar_empleado(empleado1)
empresa1.contratar_empleado(empleado2)
empresa1.contratar_empleado(empleado3)

print(f'Número de empleados en {empresa1.nombre}: {empresa1.obtener_empleados_empresa()}')
print(f'Número de empleados en informática: {empresa1.obtener_numero_empleados_departamento('Informática')}')

# Creación de la empresa
empresa2 = Empresa('NTT DATA')
print(f'\nLa empresa {empresa2.nombre} ha sido creada')

# Creación de los empleados
empleado4 = Empleado('Tiziano Barone', 'Informática')
empleado5 = Empleado('Laura García', 'Recursos Humanos')

# Contratación de los empleados a la empresa
empresa2.contratar_empleado(empleado4)
empresa2.contratar_empleado(empleado5)

print(f'Número de empleados en {empresa2.nombre}: {empresa2.obtener_empleados_empresa()}')
print(f'Número de empleados en informática: {empresa2.obtener_numero_empleados_departamento('Informática')}')