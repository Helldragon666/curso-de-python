


'''
Programa:
    - Ventana
    - Tamaño fijo
    - No redimencionable
    - Diferentes pantallas
    - Formulario de añadir productos
    - Guardar datos temporalmente
    - Mostrar datos listados en la pantalla principal
    - Opción de Salir 
'''


from tkinter import *
from tkinter import ttk


# Definir ventana
ventana = Tk()
#ventana.geometry('500x500')
ventana.minsize(500, 500)
ventana.title('Proyecto Tkinder')
ventana.resizable(0, 0)


# Definir campos de pantallas
homeLabel = Label(ventana, text='Inicio')
#productsBox = Frame(ventana, width=250)

Label(ventana).grid(row=1)
productsTable = ttk.Treeview(height=12, columns=2)
productsTable.grid(row=1, column=0, columnspan=2)
productsTable.heading('#0', text='Producto', anchor=W)
productsTable.heading('#1', text='Precio', anchor=W)

addLabel  = Label(ventana, text='Añadir producto')
infoLabel = Label(ventana, text='Información')
dataLabel = Label(ventana, text='Creado por Yonatan Charbel Cervantes Zavala - 2021')

# Variables para el formulario
nameData = StringVar()
priceData = StringVar()
products =[]

def addProduct():
    products.append([
        nameData.get(),
        priceData.get(),
        addDescripcionEntry.get('1.0', 'end-1c')
    ])

    nameData.set('')
    priceData.set('')
    addDescripcionEntry.delete('1.0', END)

    home()

# Campos del formulario

addFrame = Frame(ventana)

addNameLabel = Label(addFrame, text='Nombre:')
addNameEntry = Entry(addFrame, textvariable=nameData)

addPriceLabel = Label(addFrame, text='Precio:')
addPriceEntry = Entry(addFrame, textvariable=priceData)

addDescripcionLabel = Label(addFrame, text='Descripción:')
addDescripcionEntry = Text(addFrame)

addSeparator = Label(addFrame)

boton = Button(addFrame, text='Guardar', command=addProduct) 



# Pantallas
def home():
    # Montar pantalla
    homeLabel.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=210,
        pady=20
    )
    homeLabel.grid(row=0, column=0)
    productsTable.grid(row=2)

    # Listar productos
    '''
    for product in products:
        if len(product) == 3:
            product.append('Added')
            Label(productsBox, text=product[0]).grid()
            Label(productsBox, text=product[1]).grid()
            Label(productsBox, text=product[2]).grid()
            Label(productsBox, text='------------------').grid()
    '''

    for product in products:
        if len(product) == 3:
            product.append('Added')
            productsTable.insert('', 0, text=product[0], values=(product[1]))


    # Ocultar Pantallas 
    addLabel.grid_remove()
    addFrame.grid_remove()
    infoLabel.grid_remove()
    dataLabel.grid_remove()



def add():
    
    addLabel.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=110,
        pady=20
    )
    addLabel.grid(row=0, column=0, columnspan=16)

    addFrame.grid(row=1)

    addNameLabel.grid(row=1, column=0,padx=5, pady=5, sticky=W)
    addNameEntry.grid(row=1, column=1,padx=5, pady=5, sticky=W)

    addPriceLabel.grid(row=2, column=0,padx=5, pady=5, sticky=W)
    addPriceEntry.grid(row=2, column=1,padx=5, pady=5, sticky=W) 

    addDescripcionLabel.grid(row=3, column=0,padx=5, pady=5, sticky=NW)
    addDescripcionEntry.grid(row=3, column=1,padx=5, pady=5, sticky=W)
    addDescripcionEntry.config(
        width=30,
        height=5,
        font=('Consolas', 12),
        padx=15,
        pady=15
    )

    addSeparator.grid(row=4)

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg='black',
        fg='white'
    )    

    homeLabel.grid_remove()
    productsTable.grid_remove()
    infoLabel.grid_remove()
    dataLabel.grid_remove()

def info():
    infoLabel.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=150,
        pady=20
    )
    infoLabel.grid(row=0, column=0)

    dataLabel.grid(row=1, column=0)

    homeLabel.grid_remove()
    productsTable.grid_remove()
    addLabel.grid_remove()
    addFrame.grid_remove()



# Cargar pantalla de Inicio
home()


# Menu Principal
menuPrincipal = Menu(ventana)
menuPrincipal.add_command(label='Inicio', command=home)
menuPrincipal.add_command(label='Añadir', command=add)
menuPrincipal.add_command(label='Información', command=info)
menuPrincipal.add_command(label='Salir', command=ventana.quit)

# Cargar menu
ventana.config(menu=menuPrincipal)



# Cargar Ventana
ventana.mainloop()