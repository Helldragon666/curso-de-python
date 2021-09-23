

'''
Ejercicio 6.
    - Mostrar todas las tablas de multiplicar del 1 al 10
    - Mostrar el título de la tabla y las multiplicaciones del 1 al 10
'''

for i in range(1, 11):
    print(f'--------Tabla del {i}--------')
    for numero in range(1, 11):
        print(f'{i} x {numero} = {i * numero}')