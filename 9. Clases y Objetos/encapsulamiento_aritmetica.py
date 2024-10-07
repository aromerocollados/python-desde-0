class Aritmetica:
    
    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2
        
    @property
    def operando1(self):
        return self._operando1
    
    @property
    def operando2(self):
        return self._operando2
    
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1
    
    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2
    
    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'{self.operando1} + {self.operando2} = {resultado}')
        
    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'{self.operando1} - {self.operando2} = {resultado}')
        
    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'{self.operando1} * {self.operando2} = {resultado}')
        
    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'{self.operando1} / {self.operando2} = {resultado}')
        
aritmetica = Aritmetica(6, 3)

aritmetica.sumar()
aritmetica.restar()
aritmetica.multiplicar()
aritmetica.dividir()