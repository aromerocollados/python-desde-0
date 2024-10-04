print('*** Potencia número usando funciones recursivas ***')

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else: 
        return base * potencia(base, exponente-1)

base = int(input('Introduce la base: '))
exponente = int(input('Introduce el exponente: '))

resultado = potencia(base, exponente)
print(f'El resultado de base {base} elevado a {exponente} es igual a {resultado}')