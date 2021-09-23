


'''
LISTAS (arrays):
    - Colleciones o cunjunto de datos/valores, bajo un único nombre
    - Para acceder a esos valorres se utiliza un índice 
'''

# Definir lista
heroes = ['batman', 'spiderman', 'wolverin']
cantantes = list(('Ozuna', 'Shakira', 'Camila')) # Se debe de pasar una tupla o elementos iterables para crear una lista

years = list(range(2000, 2022))

variada = ['Yon', 20, 4.4, True, 'Texto', {
    'nombre': 'Yona',
    'edad': 20
}]

print(cantantes)

print(heroes)

print(years)

print(variada)


# Índices

# heroes[1] = 'superman' # cambiar el valor de un índice

print(heroes[1]) # valor positivo de izquierda a derecha
print(heroes[-2]) # valor negativo de derecha a izquierda

print(cantantes[1:3]) # 'Shakira', 'Camila'
print(cantantes[0:1]) # 'Ozuna'
print(cantantes[0:2]) # 'Ozuna', 'Shakira'
print(cantantes[0:3]) # 'Ozuna', 'Shakira', 'Camila'

print(heroes[1:]) # 'spiderman', 'wolverin'
print(heroes[0:]) # 'batman', 'spiderman', 'wolverin'


# Añadir elemento a lista

cantantes.append('Juan Gabriel') # solo toma 1 argumento
print(cantantes)


# Recorrer Lista

nuevoHeroe = ''

while True:
    nuevoHeroe = input('ingresa una nuevo Héroe: ')
    heroes.append(nuevoHeroe)

    nuevoHeroe = input('Desea añadir otro Héroe? (y/n): ')

    if nuevoHeroe == 'n' or nuevoHeroe == 'N':
        print('Saliendo...')
        break

print('\n***************LISTADO DE HÉROES***************')

for heroe in heroes:
    print(f'{heroes.index(heroe) + 1}. {heroe}')



# Listas multidimensionales

print('\n***************LISTADO DE CONTACTOS***************')

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]
 

print(contactos)
print(contactos[1][1]) #luis@luis.com

# for contacto in contactos:
#     print(contacto[0]) # nombres de los contactos
 
for contacto in contactos:
    for datos in contacto:

       if contacto.index(datos) == 0:
           print(f'Nombre: {datos}')
       else:
           print(f'Email: {datos}')

    print('\n')