from random import randint

print('\n*** Sistema Generador de ID Único ***')

nombre = input('Cual es tu nombre? ')
apellido = input('Cual es tu apellido? ')
ano_nacimiento = int(input('Cual es tu año de nacimiento (YYYY)? '))

valor_nombre = nombre.strip().upper()[0:2]
valor_apellido = apellido.strip().upper()[0:2]
valor_nacimiento = str(ano_nacimiento)[2:4]
valor_aleatorio = str(randint(1000, 9999))

id = valor_nombre + valor_apellido + valor_nacimiento + valor_aleatorio

print(f'Id generado: {id}')