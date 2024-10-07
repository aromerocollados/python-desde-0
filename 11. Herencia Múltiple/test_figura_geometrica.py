from cuadrado import Cuadrado
from rectangulo import Rectangulo

print('Creación Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5, 'rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(9, 8,'verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)