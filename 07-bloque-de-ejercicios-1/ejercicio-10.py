

'''
Ejercicio 10.
    - Pedir al usuario la calificacion de 
      15 alumnos
    - Mostrar en pantalla cuantos aprobaron
      y cuantos reprobaron 
'''


aprobados = 0
reprobados = 0

alumnos = int(input('Ingrese el numero de alumnos: '))

for i in range(1, alumnos + 1):
    nota = int(input(f'Ingrese la calificación del alumno {i}: '))

    if nota <= 10 and nota >= 0:
        if nota >= 6:
            aprobados += 1
        else: 
            reprobados += 1
    else:
        print('Solo se permiten notas del rango 0 - 10')

print(f'Aprobados: {aprobados} Reprobados: {reprobados}')