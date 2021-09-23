

import os, shutil

# Crear carpeta

if not os.path.isdir('./miCarpeta'):
    os.mkdir('./miCarpeta')
else:
    print('ya existe el directorio')


# Eliminar carpeta
#os.rmdir('./miCarpeta')

# Copiar carpeta

rutaOriginal = './miCarpeta'
rutaNueva = './miCarpeta(1)'

shutil.copytree(rutaOriginal, rutaNueva)

print('Contenido de miCarpeta')
contenido = os.listdir('./miCarpeta')

for fichero in contenido:
    print(f'Fichero: {fichero}')
