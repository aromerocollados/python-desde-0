print('*** Agenda de Contactos ***')

# Diccionario dentro de otro diccionario
agenda = {
    'Alejandro_Romero': {
        'telefono': '625045900',
        'email': 'alejandro@gmail.com',
        'direccion': 'direccion1'
    },
    
    'Marta_Garcia': {
        'telefono': '633453933',
        'email': 'marta@gmail.com',
        'direccion': 'direccion2'
    },
    
    'Walter_White': {
        'telefono': '644741014',
        'email': 'heisenberg@gmail.com',
        'direccion': 'Jesse\'s House'
    },
    
    'Michael_Scofield': {
        'telefono': '625045900',
        'email': 'kanieloutis@gmail.com',
        'direccion': 'Prison'
    }
}

# Acceder a la informacion de un contacto en especifico
print(f'''Información del contacto de Walter White:
    Teléfono: {agenda['Walter_White']['telefono']}
    Email: {agenda.get('Walter_White').get('email')}
    Dirección: {agenda.get('Walter_White').get('direccion')}''')

"""
# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '55678392',
    'email': 'ana@mail.com',
    'direccion':'Calle Salvador Diaz 321'
}

print(agenda)

# Eliminar un contacto existente
agenda.pop('Ana')
#del agenda['Ana']
print(agenda)

"""
# Mostramos los contactos de la agenda
print('\n---Contactos en la Agenda---')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
''')