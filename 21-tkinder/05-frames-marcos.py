

from tkinter import *

ventana = Tk()
ventana.title('Marcos | Frames')
ventana.geometry('700x700')

marco_padre = Frame(ventana, width=250, height=250)

marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg='red',
    bd=10,
    relief='solid' # o SOLID    sin las comillas
)
marco.pack(side='right', anchor=SE)
marco.pack_propagate(False)

texto = Label(marco, text='Primer Marco')
texto.config(
    bg='red',
    fg='white',
    font=('Arial', 20),
    #height=10,
    #width=10,
    #bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=BOTH, expand=YES)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg='green',
    bd=10,
    relief='solid' # o SOLID    sin las comillas
)
marco.pack(side='left', anchor=SW)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='blue',
    bd=10,
    relief='solid' # o SOLID    sin las comillas
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='orange',
    bd=10,
    relief='solid' # o SOLID    sin las comillas
)
marco.pack(side=RIGHT)



ventana.mainloop()