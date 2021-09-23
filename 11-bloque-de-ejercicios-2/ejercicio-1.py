

'''
Ejercicio 1:
    - Programa con una lista de 8 números
    - Recorrer la lista y mostarla
    - Función que recorra la lista y devuelva un str
    - Ordenar la lista y mostrarla
    - Mostrar su longitud
    - Buscar algun elemento (que el usuario ingrese)
'''


numeros = [5, 3, 2, 7, 6, 8, 1, 4]

# for numero in numeros:
#     print(numero)

print('---------------------------------------------')

def recorrerLista(array = []):
    cadena = ''
    for element in array:
        cadena += f'{element}, '
    return cadena

print(recorrerLista(numeros))

print('---------------------------------------------')
numeros.sort()

print(recorrerLista(numeros))

print('--------------------------------------------')

print(f'Longitud: {len(numeros)}')

print('---------------------------------------------')


numU = input('Ingrese el número a buscar: ')

if numU.isnumeric():
    if int(numU) in numeros:
        print(f'{numU} encontrado en índice {numeros.index(numU)}')
    else:
        print(f'{numU} no esxiste en la lista')
else :
    print(f'{numU} no es un número')