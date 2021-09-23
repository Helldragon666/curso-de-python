

'''
Diccionario:
    Tipo de dato que almacena un conjunto de datos
    en formato "clave: valor"
'''


persona = {
    'nombre': 'Yon',
    'apellido': 'Cervantes',
    'edad': 20
}


print(type(persona))
print(persona)

print(persona['nombre'])


# lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos)

print(contactos[0]['nombre'])

contactos[0]['nombre'] = 'Yonatan'
print(contactos[0]['nombre'])


print('\n***************LISTADO DE CONTACTOS***************')

for contacto in contactos:
    print('----------------------------')
    print(f'Nombre: {contacto["nombre"]}')
    print(f'Email: {contacto["email"]}')
    print('----------------------------')