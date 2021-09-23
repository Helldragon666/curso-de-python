

'''
Ejercicio 3:
    - Programa que compruebe si una variable esta vacia
    - Si esta vacia rellenarla con texto un minucula
    - Mostrar en pantalla en MAYUSCULA
'''

texto = ''

if not texto:  # len(texto.strip()) <= 0
    texto = 'HoLa'.lower()
    print(texto.upper())
else:
    print(f'la variable tiene contenido {texto}')
