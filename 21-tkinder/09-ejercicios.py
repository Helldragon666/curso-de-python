


"""
    Calculadora:
    - 2 campos de texto
    - 4 botones para las operaciones
    - Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title('*******Calculadora Básica*******')
ventana.geometry('400x400')
ventana.config(
    bd=25
)


n1 = StringVar()
n2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text='Ingrese un número:').pack()
Entry(marco, textvariable=n1, justify=CENTER).pack()


Label(marco, text='Ingrese un número:').pack()
Entry(marco, textvariable=n2, justify=CENTER).pack()

Label(marco).pack()


def sumar():
    try:
        resultado.set(float(n1.get()) + float(n2.get()))
        MessageBox.showinfo('Resultado!', f'{n1.get()} + {n2.get()} = {resultado.get()}')
    except:
        MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')


def restar():
    try:
        resultado.set(float(n1.get()) - float(n2.get()))
        MessageBox.showinfo('Resultado!', f'{n1.get()} - {n2.get()} = {resultado.get()}')
    except:
        MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')

def multiplicar():
    try:
        resultado.set(float(n1.get()) * float(n2.get()))
        #n1.set('')
        #n2.set('')
        MessageBox.showinfo('Resultado!', f'{n1.get()} x {n2.get()} = {resultado.get()}')
    except:
        MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')

def dividir():
    try:
        resultado.set(float(n1.get()) / float(n2.get()))
        MessageBox.showinfo('Resultado!', f'{n1.get()} / {n2.get()} = {resultado.get()}')
    except:
        MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')

def salir():
    respuesta = MessageBox.askquestion('Salir', 'Desea salir?')

    if respuesta == 'yes':
        ventana.destroy()



Button(marco, text='Sumar', command=sumar).pack(side=LEFT)
Button(marco, text='Restar', command=restar).pack(side=LEFT)
Button(marco, text='Multiplicar', command=multiplicar).pack(side=LEFT)
Button(marco, text='Dividir', command=dividir).pack(side=LEFT)

Button(marco, text='Salir', command=salir).pack(side=LEFT)


ventana.mainloop()