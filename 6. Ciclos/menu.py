print('*** Sistema de Administración de Cuentas ***')

salir = False

while not salir:
    print('''
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir del programa''')
    
    opcion = int(input('Elegir opción: '))
    
    if opcion == 1:
        print('\nCreando cuenta...')
    elif opcion == 2:
        print('\nEliminando cuenta...')
    elif opcion == 3:
        print('\nSaliendo del programa...')
        salir = True
    else: 
        print('\nOpción inválida, pruebe otra vez\n')