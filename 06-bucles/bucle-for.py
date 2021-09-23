

'''
    FOR

    for VARIABLE in ELEMENTO_ITERABLE
        INSTRUCCIONES
'''

#contador = 0
resultado = 0

for contador in range(0, 5):
    print(f'posición: {contador}')

    resultado += contador

print(f'resultado: {resultado}')


# Ejemplo tablas de multiplicar

numero = int(input('Introduce el número a multiplicar: '))

print(f'Tabla de multiplicar del {numero}')

for multiplo in range(0, 11):

    if numero == 45:
        print('No se permite ese numero')
        break   # para salir o cortar el bucle

    print(f'{numero} x {multiplo} = {numero * multiplo}')
else:
    print('Tabla finalizada ;3')