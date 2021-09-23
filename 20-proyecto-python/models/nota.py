


from db.conexion import cursor, database

class Nota:
    
    def __init__(self, usuario_id, titulo = '', descripcion = ''):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardarNota(self):

        sql = 'INSERT INTO notas VALUES(null, %s, %s, %s, NOW())'
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]

    def listarNotas(self):
        sql = f'SELECT * FROM notas WHERE usuario_id = {self.usuario_id}'
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminarNota(self):
        sql = f'DELETE FROM notas WHERE usuario_id ={self.usuario_id} AND titulo LIKE "%{self.titulo}%"'

        cursor.execute(sql)
        database.commit()
 
        return [cursor.rowcount, self]
