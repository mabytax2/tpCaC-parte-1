import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="labelec"
)

cursor = conexion.cursor()

tabla = "libros"
consulta = f"SELECT * FROM {tabla}"


cursor.execute(consulta)

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Mostrar los datos de la tabla
for fila in resultados:
    print(fila)

cursor.close()
conexion.close()
