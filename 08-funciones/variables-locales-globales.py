

# Varable global

frase = 'Ni los genios son tan genios, ni los mediocres tan mediocres'

print(frase)

def holaMundo():
    frase = 'Hola Mundo'
    print(frase)

    global website #para convertir una variable local a variable global 
    website = 'yonatan.com'
    print('DENTRO: ' + website)

holaMundo()

print('FUERA: ' + website)