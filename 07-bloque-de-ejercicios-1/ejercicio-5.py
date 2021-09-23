

'''
Ejercicio 5.
    - Programa que muestre todos los números entre
      2 numeros que el usuario diga
'''

n1 = int(input('Ingrese el primer número: '))

n2 = int(input('Ingrese el segundo número: '))

if n1 < n2:
    for numero in range(n1 + 1, n2):
        print(numero)
else:
    print('El primer número debe ser menor al segundo')