try: 
    archivo = open('15. Archivos/prueba.txt', 'w', encoding='UTF-8')
    archivo.write('Añadimos información al archivo')
except Exception as e:
    print(e)
finally:
    archivo.close() # Una vez cerrado no se puede trabajar con el archivo hasta que se vuelva a abrir
    
    