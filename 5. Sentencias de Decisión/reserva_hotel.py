print('*** Sistema de Reserva de Hotel ***')

SIN_VISTA_MAR = 150.50
CON_VISTA_MAR = 190.50

cliente = input('\n¿Nombre del cliente?: ')
dias_estancia = int(input('¿Cuántos días estará en el hotel?: '))
vista_al_mar = input('¿Quiere vista al mar (Si/No)?: ')
vista_al_mar = vista_al_mar.strip().lower() == 'si'

if vista_al_mar == True:
    coste_total = dias_estancia * CON_VISTA_MAR
else:
    coste_total = dias_estancia * SIN_VISTA_MAR
    
print(f'El precio final de la estancia de {cliente} es de {coste_total}€')

