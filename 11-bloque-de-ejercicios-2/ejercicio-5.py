


'''
Ejercicio 5:
    - Crear una lista con el contenido de esta tabla:
        ACCION         AVENTURA       DEPORTES
        GTA             CREDD          FIFA 21
        COD             CRASH           PRO 21
        PUBG            PRINCE         MOTO GP

    - Imprimir información ordenada
'''

def recorrerJuegos(array = []):
    cadena = ''
    for element in array:
        cadena += f'{element} '
    return cadena
    

juegos = [
    {
        'categoria': 'ACCIÓN',
        'juegos': ['GTA', 'COD', 'PUBG']
    },
     {
        'categoria': 'AVENTURA',
        'juegos': ['CREDD', 'CRASH', 'PRINCE']
    },
     {
        'categoria': 'DEPORTES',
        'juegos': ['FIFA 21', 'PRO 21', 'MOTO GP']
    }
]

for elemento in juegos:
    print(f'---------{elemento["categoria"]}---------')
    print(recorrerJuegos(elemento['juegos']))
    print('\n')