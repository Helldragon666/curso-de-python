

nombre = 15

#Func Generales

print(nombre)

# Detectar el tipado
comprobar = isinstance(nombre, str)

if not comprobar:
  print('No es una cadena')


if not isinstance(nombre, float):
    print(f'{nombre} no es float')


# Limpiar espacios

frase = '         mi contenido         '

print(frase)
print(frase.strip())


# Eliminar variables 

year = 2021

print(year)

del year
#print(year)


# Comprobar variable vacia

texto = '  ff  '

if len(texto) <= 0:
    print('Esta vacio')
else: 
    print(f'{len(texto)} caracteres de longitud' )


# Encontrar caracteres

frase = 'La vida es bella'

print(frase.find('vida'))


# Reemplazar palabras en un string

nuevaFrase = frase.replace('vida', 'moto')

print(nuevaFrase)


# Mayúsculas y minusculas

nombre = 'Yonatan'

print(nombre.lower())
print(nombre.upper())