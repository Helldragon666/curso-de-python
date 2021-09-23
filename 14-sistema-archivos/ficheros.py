

from io import open
import pathlib, shutil 

# Abrir archivo (si no exite lo crea)
ruta = str(pathlib.Path().absolute()) + '/fichero-texto.txt'

archivo = open(ruta, 'a+') # permiso a+

# Escribir en un archivo
archivo.write(f'Holi desde {ruta} ;3\n')


# Cerrar arhivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + '/fichero-texto.txt'

archivoLectura = open(ruta, 'r') # permiso r (lectura)

# Leer contenido
#contenido = archivoLectura.read()
#print(contenido)


# Leer contenido y guardar en lista
lista = archivoLectura.readlines()
archivoLectura.close()
#print(lista)

for elemento in lista:
    print(elemento)
    print(elemento.isnumeric())

# Copiar archivo
rutaOriginal = str(pathlib.Path().absolute()) + '/fichero-texto.txt'
rutaNueva = str(pathlib.Path().absolute()) + '/fichero-texto(1).txt'
shutil.copyfile(rutaOriginal, rutaNueva)


# Mover archivos
rutaOriginal = str(pathlib.Path().absolute()) + '/fichero-texto.txt' 
rutaNueva1 = str(pathlib.Path().absolute()) + '/nueva/fichero-texto-movido.txt'

shutil.move(rutaOriginal, rutaNueva1)

# Eliminar archivos
import os

rutaNueva1 = str(pathlib.Path().absolute()) + '/nueva/fichero-texto-movido.txt'
os.remove(rutaNueva1)

# Comprobar si un archivo existe

import os.path

# (os.path.abspath('./') otra forma de obtener la ruta absoluta pathlib.Path().absolute()

if os.path.isfile(os.path.abspath('./') + '/fichero-texto.txt'):
    print('existe')
else:
    print('no exite')
