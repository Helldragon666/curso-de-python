

'''
Ejercicio 7.
    - Escribir un script que muestre en pantalla
      todos los números impares entre 2 números
      que elija el usuario
'''


n1 = int(input('Ingresa el primer número: '))
n2 = int(input('Ingresa el segundo número: '))

if n1 < n2:
    for i in range(n1 + 1, n2):
        if i % 2 == 1:
            print(i)
else:
    print('El primer número debe ser menor al segundo')