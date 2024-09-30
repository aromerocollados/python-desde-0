# Inmutabilidad en cadenas
cadena1 = "Hola Mundo"
# cadena1[0] = "h"  --No podemos reemplazar los caracteres, solo es posible cambiar el valor de la cadena

cadena2 = cadena1
cadena1 = "Adios"

print(cadena1)