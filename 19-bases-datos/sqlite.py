

# Importar módulo

import sqlite3

# Conectar BD

conexion = sqlite3.connect('pruebas.db')

# Crear cursor (lo que permite ejecutar una consulta)
cursor = conexion.cursor()

# Crear Tabla
cursor.execute('CREATE TABLE IF NOT EXISTS productos(' +
'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
'titulo VARCHAR(255), ' +
'descripcion TEXT, ' +
'precio int(255)' +
')')  # tambian se puede usar el comentario multilinea para esta consulta

# Guardar cambios
conexion.commit()

#Insertar Datos
#cursor.execute('INSERT INTO productos VALUES (null, "Primer producto", "Descripcción de mi producto", 550)')
#conexion.commit()

# Borrar registros
#cursor.execute('DELETE FROM productos') # para borrar todos los registros
#conexion.commit()

#Insertar multiples registros
productos = [
    ('Laptop', 'Muy rapida', 700),
    ('Movil', 'Muy rapida', 140),
    ('Placa Base', 'Resistente', 80),
    ('Tablet', 'Muy rapida', 250)
]

#cursor.executemany('INSERT INTO productos VALUES (null, ?, ?, ?)', productos)
#conexion.commit()

# Update
cursor.execute('UPDATE productos SET precio=678 WHERE precio=80')

# Leer Datos
cursor.execute('SELECT * FROM productos')
#cursor.execute('SELECT * FROM productos WHERE precio >= 100')
productos = cursor.fetchall()

#print(productos)
for producto in productos:
    print('------------------------------------------')
    print('Titulo: ', producto[1])
    print('Descripción: ', producto[2])
    print('Precio: ', producto[3])

cursor.execute('SELECT titulo FROM productos')
producto = cursor.fetchone() #Muestra el primer registro que encuentre 
print(producto)

# Cerrar conexión
conexion.close()