

from tkinter import *

ventana = Tk()

menuVariable = Menu(ventana)
ventana.config(menu=menuVariable)

archivo = Menu(menuVariable, tearoff=0) # tearoff=0 para quitar las lineas punteadas en inicio del submenu
archivo.add_command(label='Nuevo archivo')
archivo.add_command(label='Nueva ventana')
archivo.add_separator()
archivo.add_command(label='Abrir archivo')
archivo.add_command(label='Abrir carpeta')
archivo.add_separator()
archivo.add_command(label='Salir', command=ventana.quit)

menuVariable.add_cascade(label='Archivo', menu=archivo)
menuVariable.add_command(label='Editar')
menuVariable.add_command(label='Selección')



ventana.mainloop()