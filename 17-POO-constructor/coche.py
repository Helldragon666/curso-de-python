


class Coche:

    #Atributos o propiedades (variables)
    #color = ''
    #marca = ''
    #modelo = ''
    #velocidad = 0
    #puertas = 0

    soyPublico = 'Soy un atributo publico'
    __soyPrivado = 'Soy un atributo privado' # __ antes del nombre del atributo o método para hacerlo privado

    #NUEVO: Constructor
    def __init__(self, color, marca, modelo, velocidad, puertas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.puertas = puertas

    #Métodos, acciones del objeto (funciones)
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1

    #Getter
    def getVelocidad(self):
        return self.velocidad
    def getColor(self):
        return self.color
    def getModelo(self):
        return self.modelo
    def getMarca(self):
        return self.marca
    def getPrivado(self):
        return self.__soyPrivado

    def getInfo(self):
        info = '---------Información del coche---------\n'
        info += f'Color: {self.getColor()}\n'
        info += f'Marca: {self.getMarca()}\n'
        info += f'Modelo: {self.getModelo()}\n'
        info += f'Velocidad: {self.getVelocidad()}\n'
        info += '---------------------------------------'

        return info

    #Setter
    def setColor(self, color):
        self.color = color
    def setModelo(self, modelo):
        self.modelo = modelo
    def setMarca(self, marca):
        self.marca = marca