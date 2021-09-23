

from models.usuario import Usuario 
from models.accionesNotas import AccionesNotas
# as sirve para poner in alias a las importaciones

class AccionesUsuario:

    def registro(self):

        print('\nOK!! Vamos a registrarte en el sistema...')
        nombre = input('Ingrese su nombre(s): ')
        apellidos = input('Ingrese su apellido(s): ')
        email = input('Ingrese su email: ')
        password = input('Ingrese una contraseña: ')

        usuario = Usuario(nombre, apellidos, email, password)
        registro = usuario.registrarBD()

        if registro[0] >= 1:
            print(f'Perfecto!! {registro[1].nombre} registrado con el email {registro[1].email}')
            
            login = usuario.identificarBD()
            
            self.proximasAcciones(login)
        else:
            print('No te has registrado correctamente')

    def login(self):
        print('\nVale!! Identificaque en el sistema...')
        
        try:
            email = input('Ingrese su email: ')
            password = input('Ingrese una contraseña: ')

            usuario = Usuario('', '', email, password)
            login = usuario.identificarBD()

            print(f'\nBienvenid@ {login[1]}, login hecho satisfactoriamente')

            self.proximasAcciones(login)
            
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            #print(e)
            print('Datos incorrectos')
    
    def proximasAcciones(self, usuario):
        print('''
        Acciones disponibles:
            1.- Crear Nota
            2.- Mostrar Notas
            3.- Eliminar Nota
            4.- Salir
        ''')

        accion = input('Qué desea hacer? (1, 2, 3 o 4): ')

        accionesNotas = AccionesNotas()

        if accion == '1':
            accionesNotas.crearNota(usuario)
            self.proximasAcciones(usuario)
        elif accion == '2':
            accionesNotas.mostrarNotas(usuario)
            self.proximasAcciones(usuario)
        elif accion == '3':
            accionesNotas.borrarNota(usuario)
            self.proximasAcciones(usuario)
        elif accion == '4':
            print(f'ok {usuario[1]}, hasta pronto!!')
        else:
            print('ERROR!! Escoje entre 1, 2, 3 o 4')