


cantantes = ['Drake', 'Bad Bunny', 'Rihanna', 'Shakira']
numeros = [1, 2, 5, 8, 3, 4]


# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Agregar elementos
cantantes.append('Juan Gabriel')
print(cantantes)

cantantes.insert(1, 'Julieta Venegas') # 'Drake', 'Julieta Venegas', 'Bad Bunny', 'Rihanna', 'Shakira', 'Juan Gabriel'
print(cantantes)

# Eliminar elementos
cantantes.pop(1) # 'Drake', 'Bad Bunny', 'Rihanna', 'Shakira', 'Juan Gabriel'
print(cantantes)

cantantes.remove('Drake') # 'Bad Bunny', 'Rihanna', 'Shakira', 'Juan Gabriel'
print(cantantes)

# Invertir lista
cantantes.reverse() # 'Juan Gabriel', 'Shakira', 'Rihanna', 'Bad Bunny'
print(cantantes)

# Buscar dentro de una lista
print('Juan Gabriel' in cantantes) # True

# Contar elementos
print(f'{str(len(cantantes))} cantantes') # 4

# Cuantas veces aparece un elemento en la lista
print(numeros.count(8)) # 1

# Obtener el índice de un elemento
print(cantantes.index('Bad Bunny')) # 3

# Unir listas

cantantes.extend(numeros) # 'Juan Gabriel', 'Shakira', 'Rihanna', 'Bad Bunny', 1, 2, 3, 4, 5, 8 
print(cantantes)