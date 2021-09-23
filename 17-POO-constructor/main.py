
from coche import Coche

carro = Coche('Amarillo', 'Renault', 'Clio', 150, 2)

print(carro.getInfo())

carro2 = Coche('Rojo', 'Lamborgini', 'Aventador', 380, 2)

print(carro2.getInfo())

#Detectar tipado
#carro2 = 'Holi'

if type(carro2) == Coche:
    print('Es de tipo "Coche" ;3')
else:
    print("No es de tipo Coche :''''3")



# Visibilidad

print(carro.soyPublico)
print(carro.getPrivado())