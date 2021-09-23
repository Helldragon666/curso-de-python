


from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)


def sacarAlerta():
    MessageBox.showinfo('Alerta!!!', 'Soy una alerta de info ;3 ;3 ')
    MessageBox.showwarning('Alerta!!!', 'Soy una alerta de warning :3 :3 ')
    MessageBox.showerror('Alerta!!!', 'Soy una alerta :0 :0 ')

Button(ventana, text='Mostrar Alerta!!!', command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion('Salir', 'Desea salir?')

    if resultado == 'yes':
        MessageBox.showinfo('Adiós', f'bye {nombre}')
        ventana.destroy()

Button(ventana, text='Salir', command= lambda: salir('Yon')).pack()



ventana.mainloop()