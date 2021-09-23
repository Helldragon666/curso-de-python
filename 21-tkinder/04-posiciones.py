

from tkinter import *

ventana = Tk()
#ventana.geometry('500x500')


texto = Label(ventana, text='Bienvenido a mi programa')
texto.config(
    fg='white', # color de fuente
    bg='#000000', # bg='black' # color de fondo del texto
    padx=20, #px # padding o margen a los lados
    pady=20, # padding o margen arriba y abajo
    font=('Arial', 20) # fuente (tipo de letra, tamaño de la fuente)
)
texto.pack(side=BOTTOM)

texto = Label(ventana, text='Soy Yon ;3')
texto.config(
    height=3,
    bg='orange',
    cursor='spider'
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text='Holi ;3 ;3')
texto.config(
    height=2,
    bg='red',
    cursor='circle'
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text='Holi ;3 ;3')
texto.config(
    height=2,
    bg='green',
    cursor='circle'
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text='Holi ;3 ;3')
texto.config(
    height=2,
    bg='blue',
    cursor='circle'
)
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()