


'''
    WHILE

    while CONDICIÓN:
        INSTRUCCIONES
        actualización de contador 
'''

contador = 1

while contador <= 100:
    print(f'posición: {contador}')
    contador += 1

print('-------------------------------')

contador = 1
cadena = str(0)

while contador <= 100:
    cadena += ', ' + str(contador)
    contador += 1

print(cadena)




# Ejemplo tablas de multiplicar

numero = int(input('\nIntroduce el número a multiplicar: '))

print(f'Tabla de multiplicar del {numero}')

contador = 0

while contador <= 10:
    print(f'{numero} x {contador} = {numero * contador}')
    contador += 1
else:
    print('\nTabla finalizada ;3')