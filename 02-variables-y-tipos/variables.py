

# Crear variables y asignarles un valor

texto = 'Master en Python'
texto2 = "Esto es otro texto"

numero = 45
decimal = 6.72


print(texto, texto2, numero, decimal)

print('----------------------------------')

# Cambiamos el valor de la variable

numero = 77
decimal = 8.9

print(numero, decimal)

print('----------------------------------')

# Concatenación

nombre = 'Yonatan'
apellido = 'Cervantes'

print(nombre + ' ' + apellido)
print(f'{nombre} {apellido}')
print('Hola soy {} {}'.format(nombre, apellido))