


# Programación Orientada a Objetos (POO o OOP)

# Definir una clase (molde para crear más objetos de ese tipo)

class Coche:

    #Atributos o propiedades (variables)
    color = 'rojo'
    marca = 'ferrari'
    modelo = 'aventador'
    velocidad = 300
    puertas = 2

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

    #Setter
    def setColor(self, color):
        self.color = color
    def setModelo(self, modelo):
        self.modelo = modelo
    


# Crear objetos / Instanciar la clase

coche = Coche()

print('COCHE 1:')

coche.setColor('amarillo')
coche.setModelo('Murcielago')

#print(coche.marca, coche.color)
#print('velocidad actual:', coche.velocidad)
print(coche.marca, coche.getModelo(), coche.getColor())
print('velocidad actual:', coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

#print('velocidad nueva:', coche.velocidad)
print('velocidad nueva:', coche.getVelocidad())


print('----------------------------------')

#Multiples Objetos

coche2 = Coche()

coche2.setColor('Verde')
coche2.setModelo('Gallardo')

print('COCHE 2:')

print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))


