
import datetime
import hashlib

from db.conexion import database, cursor

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrarBD(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = 'INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)' #%s para sustiir por datos dentro de una tupla
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result =  [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result


    def identificarBD(self):
        sql = 'SELECT * FROM usuarios WHERE email = %s AND password = %s'

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result