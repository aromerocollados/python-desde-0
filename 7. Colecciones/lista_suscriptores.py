print('*** Lista de Suscriptores ***')

suscriptores = set()
salir = False

while not salir:
    print('''
          1. Ingresar suscriptor
          2. Eliminar suscriptor
          3. Lista de suscriptores
          4. Salir''')
    opcion = int(input('\nElige una opción: '))
    
    if opcion == 1:
        nuevo_suscriptor = input('\nNombre del suscriptor: ')
        if nuevo_suscriptor in suscriptores: 
            print(f'{nuevo_suscriptor} ya existe en la lista de suscriptores')
        else: 
            suscriptores.add(nuevo_suscriptor)
            print(f'{nuevo_suscriptor} se ha añadido a la lista de suscriptores')
            
    elif opcion == 2:
        suscriptor_eliminar = input('\nNombre del suscriptor: ')
        if suscriptor_eliminar in suscriptores: 
            suscriptores.remove(suscriptor_eliminar)
            print(f'{suscriptor_eliminar} se ha eliminado')
        else: 
            print(f'{suscriptor_eliminar} no se puede eliminar porque no existe en la lista')
            
    elif opcion == 3: 
        print('\n***LISTA SUSCRIPTORES FINAL***')
        for suscriptor in suscriptores:
            print(f'- {suscriptor}')   
            
    elif opcion == 4: 
        print('\nSaliendo del programa...')
        salir = True
    
    else: 
        print('\nOpción no válida...prueba otra vez')
