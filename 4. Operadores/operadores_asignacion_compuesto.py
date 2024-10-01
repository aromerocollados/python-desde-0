print('*** Operadores Asignacion Compuestos ***')
a, b = 10, 15
print(f'Valor inicial a: {a}, b: {b}')

# Operador compuesto de suma +=
a += b # a = a + b = 25
print(f'Operador a += b es: {a}')

# Operador compuesto de resta -=
a = 10 # reiniciamos la variable a
a -= b # a = a - b = -5
print(f'Operador a -= b es: {a}')

# Operador compuesto de multiplicacion *=
a = 10 # reiniciamos el valor de a
a *= b # a = a * b = 150
print(f'Operador a *= b es: {a}')

# Operador compuesto de division /=
a = 10 # reiniciamos el valor de a
a /= b # a = a / b = 0.67
print(f'Operador a /= b es: {a:.2f}')
