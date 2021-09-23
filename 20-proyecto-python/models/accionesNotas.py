




from models.nota import Nota


class AccionesNotas:

    def crearNota(self, usuario):
        print(f'Ok {usuario[1]}!! Vamos a crear una nueva nota...')

        titulo = input('Introduce el Título de tu nota: ')
        descripcion = input('Introduce la descripción de tu nota: ')

        nota = Nota(usuario[0], titulo, descripcion)

        guardar = nota.guardarNota()


        if guardar[0] >= 1:
            print(f'Perfecto has guardado la nota {nota.titulo}, correctamente')
        else: 
            print(f'No se guardó la nota {titulo} correctamente')

    
    def mostrarNotas(self, usuario):
        print(f'Vale {usuario[1]}!! aqui tienes tus notas:\n')

        nota = Nota(usuario[0])
        notas = nota.listarNotas()

        for dato in notas:
            print('----------------------------')
            print(dato[2])
            print(dato[3])
            print('----------------------------')


    def borrarNota(self, usuario):
        print(f'Okey {usuario[1]}!! vamos a borrar notas')

        titulo = input('Introduce el titulo de la nota que deseas borrar: ')

        nota = Nota(usuario[0], titulo)

        eliminar = nota.eliminarNota()

        if eliminar[0] >= 1:
            print(f'Nota {nota.titulo} borrada correctamente')
        else:
            print(f'Nota {nota.titulo} no fue borrada o no fue encontrada')
