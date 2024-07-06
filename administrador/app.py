from flask import Flask, render_template, request




import pymysql
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='unlamdb'
)
cursor=connection.cursor()

################tabla libros#########################
#crear libro
def crear_libro(id,descripcion, idioma,tipo, ubicacion,instrumento_asociado):
    sql="INSERT INTO libros (id,descripcion, idioma,tipo, ubicacion,instrumento_asociado) VALUES (%,%,%,%,%,%)"
    cursor.execute(sql,(id,descripcion, idioma,tipo, ubicacion,instrumento_asociado))
    connection.commit()
    return cursor.lastrowid

# leer todos los libros
def leer_todos_libros():
    sql="SELECT * FROM libros"
    cursor.execute(sql)
    librose=cursor.fetchall()
    return librose

# actualizar libros
def actualizar_libro(id,descripcion, idioma,tipo, ubicacion,instrumento_asociado):
    sql="UPDATE libros SET id=%, descripcion=%, idioma=%, tipo=%, ubicacion=%, instrumento_asociado=%"
    cursor.execute(sql,(id,descripcion, idioma,tipo, ubicacion,instrumento_asociado))
    connection.commit()
    return "Libro actualizado con exito!!!!"

# eliminar libro
def eliminar_libro(id):
    sql="DELETE FROM libros WHERE id=%"
    cursor.execute(sql,(id))
    connection.commit()
    return "Libro borrado con exito!!!"

#################### tabla instrumentos#########################
#crear instrumento
def crear_instrumento(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificacioes, estado, ubicacion, adicionales,fecha_ingreso):
    sql="INSERT INTO instrumentos (nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificacioes, estado, ubicacion, adicionales,fecha_ingreso) VALUES (%,%,%,%,%,%,%,%,%,%,%,%,%,%)"
    cursor.execute(sql,(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificacioes, estado, ubicacion, adicionales,fecha_ingreso))
    connection.commit()
    return cursor.lastrowid

# leer todos los instrumentos
def leer_todos_instrumentos():
    sql="SELECT * FROM instrumentos"
    cursor.execute(sql)
    instrumentose=cursor.fetchall()
    return instrumentose

# actualizar instrumentos
def actualizar_instrumentos(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificacioes, estado, ubicacion, adicionales,fecha_ingreso):
    sql="UPDATE instrumentos SET nro_inv=%,cod_rec=%,tipo=%,descripcion=%,marca=%,modelo=%,sn=%,ab_rango=%,cod_manual=%, especificacioes=%, estado=%, ubicacion=%, adicionales=%,fecha_ingreso=%"
    cursor.execute(sql,(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificacioes, estado, ubicacion, adicionales,fecha_ingreso))
    connection.commit()
    return "Instrumento actualizado con exito!!!!"

# eliminar instrumentos
def eliminar_instrumento(nro_inv):
    sql="DELETE FROM instrumentos WHERE nro_inv=%"
    cursor.execute(sql,(nro_inv))
    connection.commit()
    return "instrumento borrado con exito!!!"

#################################################
#copiar para las otras tablas 
##################################################

#crud libros

app = Flask(__name__)

@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'GET':
        libros = leer_todos_libros()  # Función para leer todos los libros
        return render_template('listar-bib.html', libros=libros)
    elif request.method == 'POST':
        # Procesar el formulario para crear un nuevo libro
        descripcion = request.form['descripcion']
        autor = request.form['autor']
        editorial = request.form['editorial']
        ubicacion = request.form['ubicacion']
        crear_libro(descripcion, autor, editorial, ubicacion)  # Función para crear un nuevo libro
        return "Libro creado exitosamente"



@app.route('/instrumentos', methods=['GET', 'POST'])
def instrumentos():
    if request.method == 'GET':
        instrumentos = leer_instrumentos()  # Función para leer todos los instrumentos
        return render_template('instrumentos.html', instrumentos=instrumentos)
    elif request.method == 'POST':
        # Procesar el formulario para crear un nuevo instrumento
        descripcion = request.form['descripcion']
        tipo = request.form['tipo']
        codigo_manual = request.form['codigo_manual']
        ubicacion = request.form['ubicacion']
        crear_instrumento(descripcion, tipo, codigo_manual, ubicacion)  # Función para crear un nuevo instrumento
        return "Instrumento creado exitosamente"

if __name__ == '__main__':
    app.run(debug=True)