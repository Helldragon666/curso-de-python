

from tkinter import *

ventana = Tk()
ventana.geometry('700x700')
ventana.config(
    bd=50,
)

def setDato():
    resultado.set(dato.get())

    if len(resultado.get()) > 1:
        label.config(
            bg='green',
            fg='white'
        )

dato = StringVar()
resultado =StringVar()

Label(ventana, text='Ingresa un texto:').pack(anchor=NW)

Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text='Dato recojido: ').pack(anchor=NW)
label = Label(ventana, textvariable=resultado)
label.pack(anchor=NW)


Button(ventana, text='Mostrar Dato', command=setDato).pack(anchor=NW)


ventana.mainloop()