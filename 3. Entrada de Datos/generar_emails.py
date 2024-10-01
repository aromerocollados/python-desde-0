print('\n*** Sistema Generador de Emails ***')
nombre = input('Cual es tu nombre? ')
apellidos = input('Cuales son tus apellidos? ')
empresa = input('Nombre de tu empresa? ')
extension_dominio = input('Extension del dominio de tu empresa? ')

nombre = nombre.strip().replace(' ','.').lower()
apellidos = apellidos.strip().replace(' ','.').lower()
empresa = empresa.strip().lower().replace(' ','.')
extension_dominio = extension_dominio.lower().strip().replace(' ','.')

email = nombre + '.' + apellidos + '@' + empresa + extension_dominio

print(f'El email generado es: {email}')