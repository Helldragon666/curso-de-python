

'''
Ejercicio 2.
    - Escribir un script que muestre en pantalla
      todos los números pares del 1 al 120
'''
i = 1

while i <= 120:
    if i % 2 == 0:
        print(i)
    i += 1 


print('------------------------------------------')

#Otro Método

for numero in range(1, 121):
    if numero % 2 == 0:
        print(numero)