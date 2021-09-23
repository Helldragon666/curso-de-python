


from models.accionesUsuario import AccionesUsuario

print('''
Acciones disponibles:
    1.- Registro
    2.- Login
    3.- Salir
''')

accionesUsuario = AccionesUsuario()

accion = input('Qué desea hacer? (1, 2 o 3): ')

if accion == '1':
    accionesUsuario.registro()
elif accion == '2':
   accionesUsuario.login()
elif accion == '3':
    print('Saliendo...')
else:
    print('ERROR!! Escoje entre 1, 2 o 3')