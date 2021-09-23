

from tkinter import *

ventana = Tk()
ventana.geometry('700x400')
ventana.title('Formularios en Tkinder')



# Texto encabizado
encabezado = Label(ventana, text='Formulario en Tkinder (Python)')
encabezado.config(
    fg='white',
    bg='darkgray',
    font=('Open Sans', 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=100, ipadx=200)

# Label para el Campo
label = Label(ventana, text="Nombre:")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Campo de Texto
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, padx=5, pady=5)


# Label para el Campo
label2 = Label(ventana, text="Apellidos:")
label2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# Campo de Texto
campoTexto2 = Entry(ventana)
campoTexto2.grid(row=2, column=1, padx=5, pady=5)
campoTexto2.config(justify=LEFT, state=DISABLED)

# Label para el Campo
label3 = Label(ventana, text="Descripción:")
label3.grid(row=3, column=0, padx=5, pady=5, sticky=N)

# Textarea
campoTexto3 = Text(ventana)
campoTexto3.grid(row=3, column=1, columnspan=33)
campoTexto3.config(
    width=30, 
    height=5,
    font=('Arial', 12),
    padx=15,
    pady=15
)

# Botón
Label(ventana).grid(row=4, column=1)
boton = Button(ventana, text='Enviar')
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=10,
    pady=10,
    bg='green',
    fg='white'
)


ventana.mainloop()