print('*** Sistema Descuentos VIP ***')

NUM_PRODUCTOS_DESCUENTO = 10

cantidad_productos = int(input('¿Cuantos productos compraste hoy?: '))
membresia = input('¿Tiene membresia(SI/NO)?: ')

descuento = (cantidad_productos >= NUM_PRODUCTOS_DESCUENTO 
             and membresia.lower().strip() == 'si')

print(f'Tiene descuento: {descuento}')
