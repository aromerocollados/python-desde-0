print('*** Sistema de Empleados ***')

nombre = input('Nombre: ')
edad = int(input('Edad: '))
salario = float(input('Salario: '))
jefe_departamento = input('¿Jefe departamento (Si/No)?: ')

jefe_departamento = jefe_departamento.lower() == 'si'

print('\nDatos del empleado')
print('------------------')
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Salario: {salario}')
print(f'Jefe de Departamento: {jefe_departamento}')
