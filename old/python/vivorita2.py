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
#for fila in resultados:
    # print(fila)
    
with open("tabla.html", "w") as archivo_html:
    archivo_html.write("<html><head><title>Registros de la Tabla</title></head><body>")
    archivo_html.write("<h1>Registros de la Tabla</h1>")
    archivo_html.write("<table border='1'><tr><th>ID</th><th>Descripcion</th><th>Idioma</th><th>Tipo</th><th>ubicacion</th><th>Instrumento asociado</th></tr>")
    
    for fila in resultados:
        archivo_html.write(f"<tr><td>{fila[0]}</td><td>{fila[1]}</td><td>{fila[2]}</td><td>{fila[3]}</td><td>{fila[4]}</td><td>{fila[5]}</td><br></tr>")
    
    archivo_html.write("</table></body></html>")

print("Archivo HTML generado con los registros de la tabla.")

cursor.close()
conexion.close()
