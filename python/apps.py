import mysql.connector
db=mysql.connector.connect(
       host="localhost",
       user="tu_usuario",
       password="tu_contraseña",
       database="tu_base_de_datos"
   )
cursor = db.cursor()

@app.route('/cargar', methods=['GET', 'POST'])
def cargar_datos():
       # Lógica para cargar datos en la base de datos
       return 'Formulario de carga de datos'

@app.route('/modificar', methods=['GET', 'POST'])
def modificar_datos():
       # Lógica para modificar datos en la base de datos
       return 'Formulario de modificación de datos'

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar_datos():
       # Lógica para eliminar datos de la base de datos
       return 'Formulario de eliminación de datos'
