class Aritmetica:
    def __init__(self, operando1, operando2):
      self.operando1 = operando1
      self.operando2 = operando2
      
    def sumar(self):
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2

numeros = Aritmetica(6, 2)
print(f'\nAritmética de los números {numeros.operando1} y {numeros.operando2}')
print(f'SUMA: {numeros.sumar()}')
print(f'RESTA: {numeros.restar()}')
print(f'PRODUCTO: {numeros.multiplicar()}')
print(f'DIVISIÓN: {numeros.dividir()}')