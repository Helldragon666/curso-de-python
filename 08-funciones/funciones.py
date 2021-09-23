

'''
Función:
    Conjunto de instruccciones agrupadas baja un mismo
    nombre y puede reutilizarse invocando a la función
    tantas veces sea necesario


    '' = es opcional depente de como se estructure la función

    def miFuncion('parametros'):
        INSTRUCCIONES

    invocar la función "miFuncion"

    miFuncion('parametros') 
'''


#Ejemplo 1
print('\n################### EJEMPLO 1 ###################')

# definir función
def muestraNombre():
    print('Yonatan')
    print('Saúl')
    print('Iván')
    print('Carlos')

# invocar función
muestraNombre()


#Ejemplo 2
print('\n################### EJEMPLO 2 ###################')

def mostrarTuNombre(nombre, edad):
    print(f'Tu nombre es : {nombre} y tienes: {edad} años')
    if edad >= 18:
        print('Eres mayor de edad')


nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

mostrarTuNombre(nombre, edad)


#Ejemplo 3
print('\n################### EJEMPLO 3 ###################')

def tabla(numero):
    print(f'Tabla de Multtiplicar del {numero}')

    for i in range(11): 
        print(f'{numero} x {i} = {numero * i}')


numero = int(input('Ingrese un número: '))

tabla(numero)

#Ejemplo 3.1 tablas del 0 al 10

for tabla_n in range(11):
    tabla(tabla_n)


#Ejemplo 4
print('\n################### EJEMPLO 4 ###################')

def getEmpleado(nombre, dni = ''):
    print('EMPLEADO')
    print(f'Nombre {nombre}')

    if dni:  # if dni != ''
        print(f'DNI: {dni}')

getEmpleado('Yon')


#Ejemplo 5: Return o devolver datos
print('\n################### EJEMPLO 5 ###################')

def saludame(nombre):
    return f'hola {nombre}'

print(saludame('Yonatan Charbel'))

#Ejemplo 6
print('\n################### EJEMPLO 6 ###################')

def calculadora (num1, num2, basicos = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ''

    if basicos:
        cadena += f'Suma: {suma}'
        cadena += '\n'
        cadena += f'Resta: {resta}'
    else:
        cadena += f'Multiplicación: {multi}'
        cadena += '\n'
        cadena += f'División: {division}'

    return cadena

print(calculadora(5, 5, True)) 



#Ejemplo 7
print('\n################### EJEMPLO 7 ###################')

def getNombre(nombre):
    return f'Nombre: {nombre}'

def getApellido(apellido):
    return f'Apellido: {apellido}'

def devuelveTodo(nombre, apellido ):
    return f'{getNombre(nombre)} \n{getApellido(apellido)}' 

print(devuelveTodo('Yon', 'Cervantes'))


#Ejemplo 8: Funciones Lambda Función anómina
print('\n################### EJEMPLO 8 ###################')

dimeElYear = lambda year: f'El año es {year}'

print(dimeElYear(2021))