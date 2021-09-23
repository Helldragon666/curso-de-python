

from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry('700x500')

Label(ventana, text='Holi ;3 ;3').pack(anchor=W)

imagen = Image.open('./img/low_polygonal_wolf-wallpaper-1920x1080.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()