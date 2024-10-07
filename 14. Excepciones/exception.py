resultado = 0

a, b = 10,0

try:
  resultado = a / b
except Exception as e: # Exception procesa todas las excepciones, es una clase padre
  print(f'Ocurrió un error: {e}')