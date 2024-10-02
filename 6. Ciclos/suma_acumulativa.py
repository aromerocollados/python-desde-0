print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    acumulador_suma+=numero
    numero+=1
    
print(f'La suma de los {MAXIMO} primeros números es de {acumulador_suma}')
    
