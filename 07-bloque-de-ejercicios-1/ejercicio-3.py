

'''
Ejercicio 3.
    - Escribir un programa que muestre en pantalla
      los cuadrados de los 60 primeros números
    - Usar bucle for y while
'''

i = 0

while i <= 60:
    print(f'{i} - Cuadrado: {i * i}')
    i += 1


print('------------------------------')

for numero in range(0, 61): # range(61)
    print(f'{numero} - Cuadrado: {numero * numero}')