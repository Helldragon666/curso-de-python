

# Condicional IF

'''
    Operadores de comparación

    == igual
    != diferente o negación
    < menor que
    > mayor que
    <= menor o igual que
    >= mayor o igual que


    Operadores lógicos

    and    y
    not    no
    or     o
'''

# Ejemplo 1
print('\n############ EJEMPLO 1 ############')

color = input('Adivina cual es mi color favorito: ')

if color == 'rojo':
    print('Enhorabuena')
    print('El color es rojo')
else:
    print('Color incorrecto')


# Ejemplo 2
print('\n############ EJEMPLO 2 ############')

year = int(input('En que año estamos?: '))

if year >= 2021:
    print('Estamos de 2021 en adelante')
else:
    print('Es un año anterior a 2021')


# Ejemplo 3
print('\n############ EJEMPLO 3 ############')

nombre = 'Yon'
edad = 12
ciudad = 'barcelona'
continente = 'europa'

if edad >= 18:
    print(f'{nombre} es mayor de edad')
    if continente != 'europa':
        print('el usuario no es europeo')
    else:
        print(f'es europeo y de {ciudad}')
else:
    print(f'{nombre} no es mayor de edad')


# Ejemplo 4
print('\n############ EJEMPLO 4 ############')

dia = int(input('Introduce el numero del dia de la semana: '))

'''

if dia == 1:
    print('lunes')
else:
    if dia == 2:
        print('martes')
    else:
        if dia == 3:
            print('miércoles')
        else:
            if dia == 4:
                print('jueves')
            else:
                if dia == 5:
                    print('viernes')
                else:
                    if dia == 6:
                        print('sábado')
                    else:
                        if dia == 7:
                            print('domingo')
                        else:
                            print('error')

'''

if dia == 1:
	print('lunes')
elif dia == 2:
	print('martes')
elif dia == 3:
	print('miércoles')
elif dia == 4:
	print('jueves')
elif dia == 5:
	print('viernes')
elif dia == 6:
	print('sábado')
elif dia == 7:
	print('domingo')
else:
	print('error')


# Ejemplo 5
print('\n############ EJEMPLO 5 ############')

edad_real = 45

if edad_real >= 18 and edad_real <= 65:
    print('Esta en edad de trabajar')
else:
    print('No esta en edad de trabajar')


# Ejemplo 6
print('\n############ EJEMPLO 6 ############')

pais = 'México'

if pais == 'México' or pais == 'España' or pais == 'Colombia':
    print(f'{pais} es un país de habla hispana')
else:
    print(f'{pais} no es un país de habla hispana')


# Ejemplo 7
print('\n############ EJEMPLO 7 ############')

pais = 'España'

if not(pais == 'México' or pais == 'España' or pais == 'Colombia'):
    print(f'{pais} no es un país de habla hispana')
else:
    print(f'{pais} es un país de habla hispana')


# Ejemplo 8
print('\n############ EJEMPLO 8 ############')

pais = 'Russia'

if pais != 'México' or pais != 'España' or pais != 'Colombia':
    print(f'{pais} no es un país de habla hispana')
else:
    print(f'{pais} es un país de habla hispana')