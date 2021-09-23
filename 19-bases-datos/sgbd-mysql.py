

import mysql.connector

# Conexión a bd

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='master_python'
)

# Comprobar conexión
#print(database) # <mysql.connector.connection.MySQLConnection object at 0x0000019FC1CFED30>

cursor = database.cursor(buffered=True) #buffered=True en caso de usar el cursor para multiples consultas

# Crear bd
cursor.execute('CREATE DATABASE IF NOT EXISTS master_python')

#cursor.execute('SHOW DATABASES')

#for bd in cursor:
#    print(bd)

# Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
''')

cursor.execute('SHOW TABLES')

for tabla in cursor:
    print(tabla)



#######Insertar registro

#cursor.execute('INSERT INTO vehiculos VALUES (null, "Opel", "Astra", 18500)')
#database.commit()



#####Insertar multiples registros

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)    
]

#cursor.executemany('INSERT INTO vehiculos VALUES (null, %s, %s, %s)', coches)
#database.commit()



######Leer datos

#cursor.execute('SELECT * FROM vehiculos')
#cursor.execute('SELECT * FROM vehiculos WHERE precio <= 5000')
cursor.execute('SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = "Seat"')

resultado = cursor.fetchall()

print('---------Todos mis autos---------')
for carro in resultado:
    print(carro)
    print(f'PRECIO: {carro[3]}')
    print('---------------------')

cursor.execute('SELECT * FROM vehiculos') #Muestra el primer registro que encuentre 
result = cursor.fetchone()
print(result)


#####Borrar datos

#cursor.execute('DELETE FROM vehiculos') # para borrar todos los registros
cursor.execute('DELETE FROM vehiculos WHERE marca = "Mercedes"')
database.commit()

print(cursor.rowcount, 'elemento(s) borrados!')

######Actualizar datos
cursor.execute('UPDATE vehiculos SET modelo="León" WHERE marca="Seat"')
database.commit()

print(cursor.rowcount, 'elemento(s) actualizados!')