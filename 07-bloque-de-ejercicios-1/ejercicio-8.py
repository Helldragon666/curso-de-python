


'''
Ejercicio 8.
    - Pedir al usuario un número
    - Pedir el porcentaje para calcular
    - Mostrar el resultado 
'''

num = int(input('Ingrese un número: '))

porcentaje = int(input('Ingrese el porcentaje a calcular (0 - 100): '))

if porcentaje >= 0 and porcentaje <= 100:
    print(f'Resultado: {num * (porcentaje/100)}')
else:
    print('Ingrese un rando entre 0 - 100 en el porcentanje')