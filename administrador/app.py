#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
#from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
#from werkzeug.utils import secure_filename


#--------------------------------------------------------------------



app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            return f"Error de base de datos"
            #Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE `libros` (
            `id` varchar(8) NOT NULL,
            `descripcion` text NOT NULL,
            `idioma` text NOT NULL,
            `tipo` text NOT NULL,
            `ubicacion` text NOT NULL,
            `instrumento_asociado` text NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            ''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    def agregar_libro(self, libro_id, descripcion, idioma, tipo, ubicacion, instrumento_asociado):
               
        sql = "INSERT INTO libros (id, descripcion, idioma, tipo, ubicacion, instrumento_asociado) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (libro_id, descripcion, idioma, tipo, ubicacion, instrumento_asociado)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid

    #----------------------------------------------------------------
    def consultar_libro(self, libro_id):
        # Consultamos un libro a partir de su código
        self.cursor.execute(f"SELECT * FROM libros WHERE id = {libro_id}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_libros(self, libro_id, n_descripcion, n_idioma, n_tipo, n_ubicacion, n_instrumento_asociado):
        sql = "UPDATE libros SET libro_id=%s, n_descripcion=%s, n_idioma=%s, n_tipo=%s, n_ubicacion=%s, n_instrumento_asociado=%s"
        valores = (libro_id, n_descripcion, n_idioma, n_tipo, n_ubicacion, n_instrumento_asociado)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def listar_libros(self):
        self.cursor.execute("SELECT * FROM libros")
        libros = self.cursor.fetchall()
        return libros

    #----------------------------------------------------------------
    def eliminar_libro(self, libro_id):
        # Eliminamos un libro de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM libros WHERE id = {libro_id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_libro(self, libro_id):
        # Mostramos los datos de un producto a partir de su código
        libro = self.consultar_libro(libro_id)
        if libro:
            print("-" * 40)
            print(f"Código.....: {libro['id']}")
            print(f"Descripción: {libro['descripcion']}")
            print(f"Cantidad...: {libro['idioma']}")
            print(f"Precio.....: {libro['tipo']}")
            print(f"Imagen.....: {libro['ubicacion']}")
            print(f"Proveedor..: {libro['instrumento_asociado']}")
            print("-" * 40)
        else:
            print("Libro no encontrado.")


#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
catalogo = Catalogo(host='localhost', user='root', password='', database='unlamdb')
#catalogo = Catalogo(host='USUARIO.mysql.pythonanywhere-services.com', user='USUARIO', password='CLAVE', database='USUARIO$miapp')


# Carpeta para guardar las imagenes.
#RUTA_DESTINO = './static/imagenes/'

#Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
#RUTA_DESTINO = '/home/USUARIO/mysite/static/imagenes'


#--------------------------------------------------------------------
# Listar todos los libros
#--------------------------------------------------------------------
#La ruta Flask /libro con el método HTTP GET está diseñada para proporcionar los detalles de todos los libros almacenados en la base de datos.
#El método devuelve una lista con todos los libros en formato JSON.
@app.route("/libros", methods=["GET"])
def listar_libros():
    libros = catalogo.listar_libros()
    return jsonify(libros)


#--------------------------------------------------------------------
# Mostrar un sólo libro según su código
#--------------------------------------------------------------------
#La ruta Flask /libro/<libro_id> con el método HTTP GET está diseñada para proporcionar los detalles de un libro específico basado en su código.
#El método busca en la base de datos el libro con el código especificado y devuelve un JSON con los detalles del producto si lo encuentra, o None si no lo encuentra.
@app.route("/libros/<libro_id>", methods=["GET"])
def mostrar_libro(libro_id):
    libro = catalogo.consultar_libro(libro_id)
    if libro:
        return jsonify(libro), 201
    else:
        return "Libro no encontrado", 404


#--------------------------------------------------------------------
# Agregar un libro
#--------------------------------------------------------------------
@app.route("/libros", methods=["POST"])
#La ruta Flask `/libro` con el método HTTP POST está diseñada para permitir la adición de un nuevo libro a la base de datos.
#La función agregar_producto se asocia con esta URL y es llamada cuando se hace una solicitud POST a /libros.
def agregar_producto():
    #Recojo los datos del form
    libro_id = request.form['id']
    descripcion = request.form['descripcion']
    idioma = request.form['idioma']
    tipo = request.form['tipo']
    ubicacion = request.files['ubicacion']
    instrumento_asociado = request.form['instrumento_asociado']  
    # nombre_imagen=[""]

    
    # Genero el nombre de la imagen
    # nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
    # nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extensión.
    # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

    nuevo_id = catalogo.agregar_libro(libro_id, descripcion, idioma, tipo, ubicacion, instrumento_asociado)
    if nuevo_id:    
        # imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))

        #Si el producto se agrega con éxito, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 201 (Creado).
        return jsonify({"mensaje": "Libro agregado correctamente.", "Id": nuevo_id}), 201
    else:
        #Si el producto no se puede agregar, se devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Internal Server Error).
        return jsonify({"mensaje": "Error al agregar el libro."}), 500
    

#--------------------------------------------------------------------
# Modificar un libro según su código
#--------------------------------------------------------------------
@app.route("/libros/<id>", methods=["PUT"])
#La ruta Flask /libros/<libro_id> con el método HTTP PUT está diseñada para actualizar la información de un libro existente en la base de datos, identificado por su código.
#La función modificar_libro se asocia con esta URL y es invocada cuando se realiza una solicitud PUT a /libro/ seguido de un número (el id del libro).
def modificar_libro(libro_id):
    libro = catalogo.consultar_libro(libro_id)
    #Se recuperan los nuevos datos del formulario
   
    if libro:
        nuevo_id = request.form("id")
        nueva_descripcion = request.form("descripcion")
        nuevo_tipo = request.form("tipo")
        nuevo_idioma = request.form("idioma")
        nueva_ubicacion = request.form("ubicacion")
        nuevo_instrumento_asociado = request.form("instrumento_asociado")
    
    
    # Verifica si se proporcionó una nueva imagen
    # if 'imagen' in request.files:
    #     imagen = request.files['imagen']
    #     # Procesamiento de la imagen
    #     nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
    #     nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extensión.
    #     nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

    #     # Guardar la imagen en el servidor
    #     imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        
        # Busco el libro guardado
    # libro = catalogo.consultar_libro(libro_id)
    # if libro: # Si existe el producto...
    #         imagen_vieja = producto["imagen_url"]
    #         # Armo la ruta a la imagen
    #         ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

    #         # Y si existe la borro.
    #         if os.path.exists(ruta_imagen):
    #             os.remove(ruta_imagen)
    
    # else:
    #     # Si no se proporciona una nueva imagen, simplemente usa la imagen existente del producto
    #     producto = catalogo.consultar_producto(codigo)
    #     if producto:
    #         nombre_imagen = producto["imagen_url"]


    # Se llama al método modificar_libro pasando el id del libro y los nuevos datos.
    if catalogo.modificar_libro(nuevo_id, nueva_descripcion, nuevo_idioma, nuevo_tipo, nueva_ubicacion, nuevo_instrumento_asociado):
        
        #Si la actualización es exitosa, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
        return jsonify({"mensaje": "Libro modificado"}), 200
    else:
        #Si el producto no se encuentra (por ejemplo, si no hay ningún producto con el código dado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Libro no encontrado"}), 403



#--------------------------------------------------------------------
# Eliminar un libro según su código
#--------------------------------------------------------------------
@app.route("/libros/<libro_id>", methods=["DELETE"])
#La ruta Flask /libros/<libro_id> con el método HTTP DELETE está diseñada para eliminar un libro específico de la base de datos, utilizando su código como identificador.
#La función eliminar_libro se asocia con esta URL y es llamada cuando se realiza una solicitud DELETE a /libros/ seguido de un número (el id del libro).
def eliminar_libro(libro_id):
    # Busco el libro en la base de datos
    libro = catalogo.consultar_libro(libro_id)
    if libro: # Si el libro existe, 
            #  elimina el libro del catálogo
        if catalogo.eliminar_libro(libro_id):
            #Si el libro se elimina correctamente, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
            return jsonify({"mensaje": "libro eliminado"}), 200
        else:
            #Si ocurre un error durante la eliminación (por ejemplo, si el libro no se puede eliminar de la base de datos por alguna razón), se devuelve un mensaje de error con un código de estado HTTP 500 (Error Interno del Servidor).
            return jsonify({"mensaje": "Error al eliminar el libro"}), 500
    else:
        #Si el libro no se encuentra (por ejemplo, si no existe un libro con el codigo proporcionado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado). 
        return jsonify({"mensaje": "Libro no encontrado"}), 404

################################################################################################################

################################################################################################################
if __name__ == "__main__":
    app.run(debug=True)
