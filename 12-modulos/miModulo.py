


def mostrarMensaje(nombre = ''):
    return f'Holi {nombre} ;3'

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
    