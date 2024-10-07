from numeros_identicos import NumerosIdenticos

resultado = 0

try:
    a = int(input('Introduce el primer número: '))
    b = int(input('Introduce el segundo número: '))
    
    if a == b:
        raise NumerosIdenticos('Ambos números son iguales, no se pueden repetir')
    else:
        resultado = a / b
        print(f'Resultado final: {resultado}')
except ZeroDivisionError as e:
  print(f'No se puede realizar la división entre 0: {e}')
except TypeError as e:
  print(f'No se puede realizar la división de dos tipos de datos distintos: {e}')
except Exception as e:
  print(f'No se puede realizar la división: {e}')