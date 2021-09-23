


'''
Ejercicio 2:
    - Programa que añada valores a una lista
    - Mientras su longitud sea menor a 120
    - Mostrar en pantalla
    - Usar while y for
'''

array = []

# i = 0
# 
# while i < 120:
#     array.append(i)
#     i += 1
     

for element in range(0, 120):
    if len(array) < 120:
        array.append(element)


print(array)
print(len(array))



