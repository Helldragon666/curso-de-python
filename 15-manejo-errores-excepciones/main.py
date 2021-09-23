'''
    Capturar excepciones y manejar errores en código
    suceptible a fallos o errores
'''

try:
    nombre = input('Ingrese su nombre: ')

    if len(nombre) > 1:
        nomUsuario = f'el nombre es: {nombre}'

    print(nomUsuario)
except:  # si hay un error o excepción
    print('Ha ocurrido un error, introduce bien el nombre')
else:  # no se ejecutará si falla el programa
    print('Todo ha funcionado correctamente')
finally:  # se ejecutará si falla o no falla el programa
    print('fin del programa')


# Multiples excepciones

try:
    numero = int(input('Número a elevar al cuadrado:'))
    print('Cuadradado de ' + str(numero) + ' es : ' + str(numero*numero))
except TypeError:
    print('Debes convertir tus cadenas a números en el código')
# except ValueError:
#    print('Introduce un número')
except Exception as e:
    print(e)  # invalid literal for int() with base 10: 'lo que introdujo el usuario'
    print(type(e))  # <class 'ValueError'>
    # Ha ocurrido un error: ValueError
    print('Ha ocurrido un error:', type(e).__name__)


# Excepciones personalizadas o lanzar excepción

try:
    edad = int(input('introduce tu edad: '))
    nombre2 = input('introduce tu nombre: ')

    if edad < 5 or edad > 110:
        raise ValueError('La edad introducida no es real')
    elif len(nombre2) < 1:
        raise ValueError('el nombre no es válido')
    else:
        print(f'Bienvenido {nombre2}')
except ValueError:
    print('introduce los datos correctamente')
except Exception as e:
    print('Existe un error:', e)
