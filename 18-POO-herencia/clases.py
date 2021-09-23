# Herencia: posibilidad de compartir métodos y atributos entre clases

class Persona(object):
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return 'Holi ;3'
    
    def caminar(self):
        return 'Caminando ;3'
    
    def dormir(self):
        return 'durmiendo ZZZzzzz'


class Informatico(Persona):
    def __init__(self):
        self.lenguajes = 'HTML, CSS, JAVASCRIPT, PHP'
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes += lenguajes
        return self.lenguajes

    def programar(self):
        return 'Estoy programando'

    def repararPC(self):
        return 'He reparado tu ordenador'


class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() #Para acceder al constructor de la clase padre
        self.auditarRedes = 'experto'
    def auditoria(self):
        return 'Estoy auditando una red'
