#from multiprocessing.connection import Connection
from flask import Flask, render_template, request


#Connection.close()

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
def crear_instrumento(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso):
    sql="INSERT INTO instrumentos (nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso) VALUES (%,%,%,%,%,%,%,%,%,%,%,%,%,%)"
    cursor.execute(sql,(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso))
    connection.commit()
    return cursor.lastrowid

# leer todos los instrumentos
def leer_todos_instrumentos():
    sql="SELECT * FROM instrumentos"
    cursor.execute(sql)
    instrumentose=cursor.fetchall()
    return instrumentose

# actualizar instrumentos
def actualizar_instrumentos(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso):
    sql="UPDATE instrumentos SET nro_inv=%,cod_rec=%,tipo=%,descripcion=%,marca=%,modelo=%,sn=%,ab_rango=%,cod_manual=%, especificaciones=%, estado=%, ubicacion=%, adicionales=%,fecha_ingreso=%"
    cursor.execute(sql,(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso))
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
        id = request.form['id']
        descripcion = request.form['descripcion']
        idioma = request.form['idioma']
        tipo = request.form['tipo']
        ubicacion = request.form['ubicacion']
        instrumento_asociado = request.form['instrumento_asociado']
        
        crear_libro(id,descripcion, idioma,tipo, ubicacion,instrumento_asociado)  # Función para crear un nuevo libro
        return "Libro creado exitosamente"



@app.route('/instrumentos', methods=['GET', 'POST'])
def instrumentos():
    if request.method == 'GET':
        instrumentos = leer_todos_instrumentos()  # Función para leer todos los instrumentos
        return render_template('instrumentos.html', instrumentos=instrumentos)
    elif request.method == 'POST':
        # Procesar el formulario para crear un nuevo instrumento
        nro_inv = request.form['nro_inv']
        cod_rec = request.form['cod_rec']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        marca = request.form['marca']
        modelo = request.form['modelo']
        sn = request.form['sn']
        ab_rango = request.form['ab_rango']
        cod_manual = request.form['cod_manual']
        especificaciones = request.form['especificaciones']
        estado = request.form['estado']
        ubicacion = request.form['ubicacion']
        adicionales = request.form['adicionales']
        fecha_ingreso = request.form['fecha_ingreso']
      
        crear_instrumento(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso)  # Función para crear un nuevo instrumento
        return "Instrumento creado exitosamente"

@app.route('/notebooks', methods=['GET', 'POST'])
def notebooks():
    if request.method == 'GET':
        notebooks = leer_todos_notebooks()  # Función para leer todos las notebooks
        return render_template('notebooks.html', notebooks=notebooks)
    elif request.method == 'POST':
        # Procesar el formulario para crear un nuevo instrumento
        nro_inv = request.form['nro_inv']
        cod_rec = request.form['cod_rec']
        marca = request.form['marca']
        modelo = request.form['modelo']
        sn = request.form['sn']
        estado = request.form['estado']
        ubicacion = request.form['ubicacion']
        vga = request.form['vga']
        hdmi = request.form['hdmi']
        s_op = request.form['s_op']
        adicionales = request.form['adicionales']
        fecha_ingreso = request.form['fecha_ingreso']
        lectora_dvd = request.form['lectora_dvd']
      
        crear_notebook(nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, vga, hdmi, s_op, adicionales, lectora_dvd, fecha_ingreso )  # Función para crear un nuevo instrumento
        return "Notebook creada exitosamente"
    
@app.route('/proyectores', methods=['GET', 'POST'])
def proyectores():
    if request.method == 'GET':
        proyectores = leer_todos_proyectores()  # Función para leer todos los proyectores
        return render_template('proyectores.html', proyectores=proyectores)
    elif request.method == 'POST':
        # Procesar el formulario para crear un nuevo proyector
        nro_inv = request.form['nro_inv']
        cod_rec = request.form['cod_rec']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        marca = request.form['marca']
        modelo = request.form['modelo']
        sn = request.form['sn']
        ab_rango = request.form['ab_rango']
        cod_manual = request.form['cod_manual']
        especificaciones = request.form['especificaciones']
        estado = request.form['estado']
        ubicacion = request.form['ubicacion']
        adicionales = request.form['adicionales']
        fecha_ingreso = request.form['fecha_ingreso']
      
        crear_proyector(nro_inv,cod_rec,tipo,descripcion,marca,modelo,sn,ab_rango,cod_manual, especificaciones, estado, ubicacion, adicionales,fecha_ingreso)  # Función para crear un nuevo instrumento
        return "proyector creado exitosamente"
if __name__ == '__main__':
    app.run(debug=True)
    
    connection.close()