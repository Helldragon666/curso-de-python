

# Tkinder:
# Modulo para crear interfaces gráficas de usuario

import os.path
from pathlib import Path
from tkinter import *

# Crear ventana raíz
ventana = Tk()

# Titulo de la ventana
ventana.title('Interfaz gráfica')

### Icono de la ventana

#rutaAbsoluta = os.path.abspath('./img/gallery_images_landscape_picture_7312.ico')
rutaAbsoluta = Path('./img/gallery_images_landscape_picture_7312.ico').absolute()

    #Mostrar texto en el programa
texto = Label(ventana, text=rutaAbsoluta)
texto.pack()

rutaRelativa = './img/gallery_images_landscape_picture_7312.ico'

ventana.iconbitmap(rutaAbsoluta) # tambien se puede usar la ruta relativa

# Cambio en el tamaño de la vantana
ventana.geometry('1920x1080')

# Bloquear el tamaño de la ventana
ventana.resizable(0, 1) # el 0 no deja redimencionar la ventana



# Arrancar y mostrar ventana hasta que se cierre
ventana.mainloop()