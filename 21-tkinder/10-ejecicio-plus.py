


"""
    Calculadora:
    - 2 campos de texto
    - 4 botones para las operaciones
    - Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox


class Calculadora:

    def __init__(self):
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.resultado = StringVar()

    def sumar(self):
        try:
            self.resultado.set(float(self.n1.get()) + float(self.n2.get()))
            MessageBox.showinfo('Resultado!', f'{self.n1.get()} + {self.n2.get()} = {self.resultado.get()}')
        except:
            MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')


    def restar(self):
        try:
            self.resultado.set(float(self.n1.get()) - float(self.n2.get()))
            MessageBox.showinfo('Resultado!', f'{self.n1.get()} - {self.n2.get()} = {self.resultado.get()}')
        except:
            MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')

    def multiplicar(self):
        try:
            self.resultado.set(float(self.n1.get()) * float(self.n2.get()))
            MessageBox.showinfo('Resultado!', f'{self.n1.get()} x {self.n2.get()} = {self.resultado.get()}')
        except:
            MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')

    def dividir(self):
        try:
            self.resultado.set(float(self.n1.get()) / float(self.n2.get()))
            MessageBox.showinfo('Resultado!', f'{self.n1.get()} / {self.n2.get()} = {self.resultado.get()}')
        except:
            MessageBox.showerror('Error!!!', 'Los datos ingresados no son números')

    def salir(self):
        respuesta = MessageBox.askquestion('Salir', 'Desea salir?')

        if respuesta == 'yes':
            ventana.destroy()





ventana = Tk()
ventana.title('*******Calculadora Básica*******')
ventana.geometry('400x400')
ventana.config(bd=25)


calculadora = Calculadora()


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
Entry(marco, textvariable=calculadora.n1, justify=CENTER).pack()


Label(marco, text='Ingrese un número:').pack()
Entry(marco, textvariable=calculadora.n2, justify=CENTER).pack()

Label(marco).pack()


Button(marco, text='Sumar', command=calculadora.sumar).pack(side=LEFT)
Button(marco, text='Restar', command=calculadora.restar).pack(side=LEFT)
Button(marco, text='Multiplicar', command=calculadora.multiplicar).pack(side=LEFT)
Button(marco, text='Dividir', command=calculadora.dividir).pack(side=LEFT)

Button(marco, text='Salir', command=calculadora.salir).pack(side=LEFT)


ventana.mainloop()