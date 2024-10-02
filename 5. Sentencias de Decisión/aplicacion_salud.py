print('*** Aplicación de Salud y Fitness ***')

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 

nombre_usuario = input('Cuál es tu nombre?: ')
nombre_usuario = nombre_usuario.upper()
pasos_diarios = int(input('Cuántos pasos has caminado hoy?: '))

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

meta_alcanzada = f'{nombre_usuario} cumplió la meta' if pasos_diarios >= META_PASOS_DIARIO else f'{nombre_usuario} no cumplió la meta'

print(f'\nDATOS DE {nombre_usuario}')
print('------------------------')
print(f'Calorías Quemadas: {calorias_quemadas} kcal')
print(f'\n{meta_alcanzada}')