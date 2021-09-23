

'''
Ejercicio 4.
    - Pedir 2 números al usuario
    - Realizar operaciones básicas de una calculadora
    - Mostrarlo por pantalla
'''


try:
    n1 = float(input('Ingrese el primer número: '))

    n2 = float(input('Ingrese el segundo número: '))
except:
    print('ingrese un número')
else:
    suma = n1 + n2
    resta= n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2

    print('####################### CALCULADORA #######################')
    print(f'Suma: {suma} Resta: {resta} Multiplicación: {multiplicacion} División: {division}')
