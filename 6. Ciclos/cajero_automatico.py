print('*** Aplicación de Cajero Automático ***')

saldo_inicial = 1000
salir = False

while not salir:
    print('''
      1. Ingresar
      2. Retirar 
      3. Consultar saldo
      4. Salir del cajero''')

    opcion = int(input('Elige una opción (1/4): '))
    
    if opcion == 1:
        cantidad_ingreso = int(input('\n¿Cuanto quiere ingresar?: '))
        saldo_inicial += cantidad_ingreso
        print(f'\nDinero ingresado correctamente, dispones de {saldo_inicial}€') 
    elif opcion == 2:
        cantidad_retiro = int(input('¿Cuanto quiere retirar?: '))
        saldo_inicial -= cantidad_retiro
        print(f'\nDinero retirado correctamente, dispones de {saldo_inicial}€') 
    elif opcion == 3:
        print(f'\nTienes en el banco {saldo_inicial}€')
    elif opcion == 4:
        print('\nSaliendo de la aplicación...')
        salir = True
    else:
        print('\n---Elige una opción válida---')