

nada = None
cadena = 'Hola soy Yon'
entero = 99
flotante = 4.2
booleano = True
arreglo = [10, 'holi'] # o conocido como lista
tupla = ('Yon', 15, 'Cerv') # como una lista pero sus valores no cambian
diccionario = {
    'nombre': 'Yon',
    'apellido': 'Cervantes',
    'edad': 20
}
rango = range(9) # range (0, 9)
dato_byte = b'Probando'



print(nada)

# tipo de dato
print(type(nada)) # NoneType
print(type(cadena)) # str
print(type(entero)) # int
print(type(flotante)) # float
print(type(booleano)) # bool
print(type(arreglo)) # list
print(type(tupla)) # tuple
print(type(diccionario)) # dict 
print(type(rango)) # range
print(type(dato_byte)) # bytes


texto = 'hola' + ' ' + str(10)

print(texto)