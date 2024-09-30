# Generador de  emails --> Resultado final: ubaldo.acosta.soto@globalmentoring.com.mx
print('*** Generador de Emails ***')

nombre = ' Ubaldo Acosta Soto   '
empresa = ' Global Mentoring '
dominio = '.com.mx'

print('Nombre usuario: ' + nombre)

nombre_normalizado = nombre.lower().strip().replace(' ', '.')
print('Nombre usuario normalizado: ' + nombre_normalizado)
print('\nNombre empresa: ' + empresa)
print('Extensión del dominio: ' + dominio)

email_normalizado = '@' + empresa.lower().strip().replace(' ', '') + dominio
print('Dominio de email normalizado: ' + email_normalizado)

email_final = nombre_normalizado + email_normalizado
print('Email final generado: ' + email_final)