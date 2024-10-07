from ManejoArchivos import ManejoArchivos

# with open('prueba.txt','r', encoding='utf8') as archivo:
with ManejoArchivos('15. Archivos/prueba.txt') as archivo:
    print(archivo.read())