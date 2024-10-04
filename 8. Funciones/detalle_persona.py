print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave-valor dict
def detalles_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')
        
detalles_persona(nombre = 'Alejandro', edad = 21)
detalles_persona(telefono = 625044848, nombre = 'Marta')
detalles_persona(casado = True, edad = 25)