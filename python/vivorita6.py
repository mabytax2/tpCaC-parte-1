import mysql.connector

# Conectarse a la base de datos MySQL
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="labelec"
)

class Registros:
    
    def __init__(self, id, descripcion,idioma,tipo,ubicacion,inst_asociado):
        self.id=id
        self.descripcion=descripcion
        self.idioma=idioma
        self.tipo=tipo
        self.ubicacion=ubicacion
        self.inst_asociado=inst_asociado
        
    def __str__(self):
        return f"ID={self.id}\n DESCRIPCION={self.descripcion}\n IDIOMA={self.idioma}\n TIPO={self.tipo}\n UBICACION={self.ubicacion}\n INSTRUMENTO ASOCIADO={self.inst_asociado}"
    
    def __del__(self):
       # print(f"ID={self.id}\n DESCRIPCION={self.descripcion}\n IDIOMA={self.idioma}\n TIPO={self.tipo}\n UBICACION={self.ubicacion}\n INSTRUMENTO ASOCIADO={self.inst_asociado}")
        print(f"El registro esta eliminado...")
        
cursor = conexion.cursor()

# Consulta SQL para seleccionar todos los registros de tu tabla
consulta = "SELECT * FROM tu_tabla"
cursor.execute(consulta)

# Obtener todos los registros y guardarlos en un array
registro_array = []
for (id, descripcion, idioma, tipo, ubicacion, inst_asociado) in cursor:
    registro = Registros(id, descripcion, idioma, tipo, ubicacion, inst_asociado)
    registro_array.append(registro)

# Cerrar cursor y conexión a la base de datos
cursor.close()
conexion.close()

# Imprimir los registros del array
for registro in registro_array:
    print(registro)
