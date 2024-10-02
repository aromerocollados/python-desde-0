print('*** Sistema Tienda en Línea con Descuentos ***')

MONTO_COMPRA_DESC = 1000

precio_compra = int(input('¿Cúal es el precio final de tu compra?: '))
miembro_tienda = input('¿Eres miembro de la tienda(SI/NO)?: ')

miembro_tienda = miembro_tienda.strip().lower() == 'si'

if precio_compra >= MONTO_COMPRA_DESC and miembro_tienda == True:
    dto = 10
elif miembro_tienda == True:
    dto = 5 
else:
    dto = 0
    
print(f'\nEl descuento que has obtenido es de {dto}%')