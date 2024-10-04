print('*** Sistema de Inventarios (con funciones) ***')

salir = False
inventario = [
    {
        'nombre': 'Producto1',
        'precio': 12.5,
        'cantidad': 10
    },
    {
        'nombre': 'Producto2',
        'precio': 30.02,
        'cantidad': 8
    },
    {
        'nombre': 'Producto3',
        'precio': 10.8,
        'cantidad': 60
    },
    {
        'nombre': 'Producto4',
        'precio': 8.8,
        'cantidad': 45
    }
]

def agregar(nombre, precio, cantidad):
    global inventario
    producto = {}
    producto['nombre'] = nombre
    producto['precio'] = precio
    producto['cantidad'] = cantidad
    
    inventario.append(producto)
    print(f'\nProducto añadido correctamente')
    # print(inventario)
    
def borrar(id):
    global inventario
    if id > 0 and id >= len(inventario):
        print('No se ha encontrado ningún producto con ese ID')
    else:
        inventario.pop(id)
        print(f'Se ha eliminado el producto con id {id}')
            
def mostrar_id(id):
    global inventario
    if id > 0 and id >= len(inventario):
        print('No se ha encontrado ningún producto con ese ID')
    else:
        producto = inventario[id]
        print(f'\nId: {inventario.index(producto)}')
        print(f'Nombre: {producto.get('nombre')}')
        print(f'Precio: {producto.get('precio')}')
        print(f'Cantidad: {producto.get('cantidad')}')
        
def mostrar():
    for producto in inventario:
        print(f'\nId: {inventario.index(producto)}')
        print(f'Nombre: {producto.get('nombre')}')
        print(f'Precio: {producto.get('precio')}')
        print(f'Cantidad: {producto.get('cantidad')}')
    
        
def menu(opcion):
    if opcion == 1:
        nombre = input('\nNombre del producto: ')
        precio = float(input('Precio: '))
        cantidad = int(input('Cantidad: '))
        agregar(nombre, precio, cantidad)
        
    elif opcion == 2:
        id = int(input('Selecciona el ID del producto que quiera borrar: '))
        borrar(id)
        
    elif opcion == 3:
        id = int(input('Selecciona el ID del producto que quiera buscar: '))
        mostrar_id(id)
        
    elif opcion == 4:
        mostrar()
        
    elif opcion == 5: 
        global salir
        salir = True

    else: 
        print(f'La opción {opcion} no es válida, prueba otra vez')
               
while salir == False:
    print('''
            1. Agregar producto
            2. Eliminar producto
            3. Buscar por ID
            4. Mostrar inventario
            5. Salir''')

    opcion = int(input('\nElige una opción: '))
    menu(opcion)