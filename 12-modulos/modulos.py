

'''
Módulos: funcionalidades ya hechas para reutilizar

    Hay módulos propios del lenguaje
    Hechos por otras personas (terceros)
    O tambien módulos creados por nosotros
'''

# Importar modulo propio

# import miModulo
# print(miModulo.mostrarMensaje('Yon'))
# print(miModulo.calculadora(3, 3, True))

from miModulo import calculadora, mostrarMensaje
#from miModulo import * # para importar todo lo que haya en el módulo

print(mostrarMensaje('Yon'))
print(calculadora(3, 3, True))


# Módulo Fechas

import datetime

print(datetime.date.today()) # fecha actual example: 2021-07-27

fechaCompleta = datetime.datetime.now()

print(fechaCompleta) # example: 2021-07-27 15:28:10.543671
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)
print(fechaCompleta.hour)


fechaPersonalizada = fechaCompleta.strftime('%d/%m/%Y, %H:%M:%S' )
print(fechaPersonalizada)


# Módulo Matemáticas

import math
print('Raíz cuandrada de 10:', math.sqrt(10))
print('PI:', math.pi)
print('Redondear (arriba):', math.ceil(6.4545)) # 7
print('Redondear (abajo):', math.floor(6.4545)) # 6

# Módulo random

import random
print('Número aleatorio (15-67): ', random.randint(15, 67))
