

from tkinter import *

ventana = Tk()
ventana.geometry('800x400')

encabezado = Label(ventana, text='Formularios 2')
encabezado.config(
    padx=15,
    pady=15,
    fg='white',
    bg='green',
    font=('Consolas', 20)
)
encabezado.pack(anchor=CENTER, fill=X)


#Checkbox

def mostrarProfesion():
    texto = ''

    if movil.get() and web.get():
        texto += 'Desarrollo Web y Desarrollo Movil'
    elif web.get():
        texto += 'Desarrollo Web'
    elif movil.get():
        texto += 'Desarrollo Movil'

    mostrar.config(text=texto, bg='green', fg='white')


web = IntVar()
movil = IntVar()

Label(ventana, text='A que te dedicas?').pack(anchor=NW)
Checkbutton(
    ventana, 
    text='Desarrollo Web',
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).pack(anchor=NW)
Checkbutton(
    ventana, 
    text='Desarrollo Movil',
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).pack(anchor=NW)

mostrar = Label(ventana)
mostrar.pack(anchor=NW)


#Radiobutton

def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None) # Para evitar qeu esten marcados ambos radiobuttons al iniciar el programa

Label(ventana, text='Sexo:').pack(anchor=NW)

Radiobutton(
    ventana, 
    text='Masculino',
    value='Masculino',
    variable=opcion,
    command=marcar
).pack(anchor=NW)
Radiobutton(
    ventana,
    text='Femenino',
    value='Femenino',
    variable=opcion,
    command=marcar
).pack(anchor=NW)

marcado = Label(ventana)
marcado.pack(anchor=NW)


#Option menu

def mostrarOpcion():
    seleccionado.config(text=respuesta.get())

respuesta = StringVar()
respuesta.set('Opción 1')

Label(ventana, text='Seleccione una opción').pack(anchor=NW)

OptionMenu(
    ventana,
    respuesta,
    'Opción 1',
    'Opción 2',
    'Opción 3'
).pack(anchor=NW)

Button(ventana, text='Ver', command=mostrarOpcion).pack(anchor=NW)

seleccionado = Label(ventana)
seleccionado.pack(anchor=NW)

ventana.mainloop()