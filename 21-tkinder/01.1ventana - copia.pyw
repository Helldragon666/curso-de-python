

from pathlib import Path
from tkinter import *

class Programa:

   def __init__(self):
     self.title = 'Master en Python'
     self.icon = Path('./img/gallery_images_landscape_picture_7312.ico').absolute()
     self.size = '770x470'
     self.redimencionable = False

   def cargar(self):
      ventana = Tk()
      self.ventana = ventana

      ventana.title(self.title)

      texto = Label(ventana, text=self.icon)
      texto.pack()

      ventana.iconbitmap(self.icon)

      ventana.geometry(self.size)

      if self.redimencionable:
         ventana.resizable(1, 1)
      else:
         ventana.resizable(0, 0)


   def addTexto(self, dato = 'holi desde un método ;3 ;3'):
      texto = Label(self.ventana, text = dato)
      texto.pack()
   
   def mostrar(self):
      self.ventana.mainloop()



programa = Programa()
programa.cargar()
programa.addTexto()
programa.addTexto('que tal ;3')
programa.mostrar()
