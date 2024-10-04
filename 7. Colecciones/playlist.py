print('*** Playlist de Canciones ***')

lista_canciones = []
numero_canciones = int(input('¿Cuántas canciones desea añadir?: '))

for i in range(1, numero_canciones+1):
    cancion = input(f'Introduce la canción {i}: ')
    lista_canciones.append(cancion)
    
print('\n---LISTA DE CANCIONES---')
    
for canciones in lista_canciones:
    print(f'''- {canciones}''')