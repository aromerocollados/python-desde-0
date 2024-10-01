# Sistema autenticación de usuario

USUARIO_CONST = 'admin'
PASSWD_CONST = '1234'

usuario = input('¿Cúal es tu usuario?: ')
passwd = input('¿Cúal es tu contraseña?: ')

datos_correctos = usuario.strip().lower() == USUARIO_CONST and passwd.strip().lower() == PASSWD_CONST

print(f'¿Datos correctos?: {datos_correctos}')