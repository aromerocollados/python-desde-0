print('*** Sistema Prestamo de Libros ***')

DISTANCIA_KM = 3

credencial = input('¿Tiene credencial de estudiante?: ')
distancia = int(input('¿A que distancia vives?: '))

prestar_libro = credencial.strip().lower() == 'si' or distancia <= DISTANCIA_KM

print(f'¿Está permitido dejarle un libro?: {prestar_libro}')