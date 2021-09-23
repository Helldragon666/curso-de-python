


'''
Ejercicio 4:
    - Programa que tenga 4 variables (lista, string, entero, booleano)
    - Imprimir En mensaje segun el tipo de dato de cada variable
'''

array = []
texto = ''
entero = 0
booleano = False

def traducirTipo(tipo):
    if tipo == list:
        return f'lista'
    elif tipo == str:
        return f'cadena de texto'
    elif tipo == int:
        return f'número entero'
    elif tipo == bool:
        return f'booleano'
    else:
        return f'no esta comtenplado el tipo {tipo}'

def mostrarTipo(variable, tipo):
    test = isinstance(variable, tipo)
    if test:
        return f'{variable} es de tipo {traducirTipo(tipo)}'
    else:
        return f'{variable} no es de tipo {traducirTipo(tipo)}'

print(mostrarTipo(array, list))
print(mostrarTipo(texto, str))
print(mostrarTipo(entero, int))
print(mostrarTipo(booleano, bool))