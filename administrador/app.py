#from multiprocessing.connection import Connection
from flask import Flask, redirect, render_template, request, url_for


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

# buscar libros
def buscar_libro(id):
    sql="select * from libros where id=%"
    cursor.execute(sql, (id))
    libro = cursor.fetchone()
    if libro:
        return libro
    else:
        return "Libro no encontrado"


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

# buscar instrumento
def buscar_instrumento(nro_inv):
    sql="select * from instrumentos where nro_inv=%"
    cursor.execute(sql, (nro_inv))
    instrumento = cursor.fetchone()
    if instrumento:
        return instrumento
    else:
        return "Instrumento no encontrado"



# eliminar instrumentos
def eliminar_instrumento(nro_inv):
    sql="DELETE FROM instrumentos WHERE nro_inv=%"
    cursor.execute(sql,(nro_inv))
    connection.commit()
    return "instrumento borrado con exito!!!"

  #################### tabla proyectores #########################

    # Crear proyector 
def crear_proyector(nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_ingreso, vga, hdmi, adicionales):
    sql = "INSERT INTO proyectores (nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_ingreso, vga, hdmi, adicionales) VALUES (%, %, %, %, %, %, %, %, %, %, %)"
    cursor.execute(sql, (nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_ingreso, vga, hdmi, adicionales))
    connection.commit()
    return cursor.lastrowid

# Leer todos los proyectores
def leer_todos_proyectores():
    sql = "SELECT * FROM proyectores"
    cursor.execute(sql)
    proyectorese = cursor.fetchall()
    return proyectorese

# Actualizar proyector 
def actualizar_proyector(nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_ingreso, vga, hdmi, adicionales):
    sql = "UPDATE proyectores SET nro_inv=%, cod_rec=%, marca=%, modelo=%, sn=%, estado=%, ubicacion=%, fecha_ingreso=%, vga=%, hdmi=%, adicionales=%"
    cursor.execute(sql, (nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_ingreso, vga, hdmi, adicionales))
    connection.commit()
    return "Proyector actualizado con éxito!"

# Eliminar proyector
def eliminar_proyector(nro_inv):
    sql = "DELETE FROM proyectores WHERE nro_inv=%"
    cursor.execute(sql, (nro_inv,))
    connection.commit()
    return "Proyector borrado con éxito!"

# buscar proyector
def buscar_proyector(nro_inv):
    sql="select * from proyectores where nro_inv=%"
    cursor.execute(sql, (nro_inv))
    proyector = cursor.fetchone()
    if proyector:
        return proyector
    else:
        return "Proyector no encontrado"

#################### tabla notebooks#########################
# Crear notebook
def crear_notebook(nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_Ingreso, vga, hdmi, adicionales, s_op, lectora_DVD):
    sql = "INSERT INTO notebooks (nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_Ingreso, vga, hdmi, s_op, adicionales, lectora_DVD) VALUES (%, %, %, %, %, %, %, %, %, %, %, %, %)"
    cursor.execute(sql, (nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_Ingreso, vga, hdmi, s_op, adicionales, lectora_DVD))
    connection.commit()
    return cursor.lastrowid

# Leer todos los notebooks
def leer_todos_notebooks():
    sql = "SELECT * FROM notebooks"
    cursor.execute(sql)
    notebookse = cursor.fetchall()
    return notebookse

# Actualizar notebooks
def actualizar_notebook(nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_Ingreso, vga, hdmi, s_op, adicionales, lectora_DVD):
    sql = "UPDATE notebooks SET nro_inv=%, cod_rec=%, marca=%, modelo=%, sn=%, estado=%, ubicacion=%, fecha_Ingreso=%, vga=%, hdmi=%, s_op=%, adicionales=%, lectora_DVD=%"
    cursor.execute(sql, (nro_inv, cod_rec, marca, modelo, sn, estado, ubicacion, fecha_Ingreso, vga, hdmi, s_op, adicionales, lectora_DVD))
    connection.commit()
    return "Notebook actualizado con éxito!"

# buscar notebook
def buscar_notebook(nro_inv):
    sql="select * from notebooks where nro_inv=%"
    cursor.execute(sql, (nro_inv))
    notebook = cursor.fetchone()
    if notebook:
        return notebook
    else:
        return "Notebook no encontrada"

# Eliminar notebooks
def eliminar_notebook(nro_inv):
    sql = "DELETE FROM notebooks WHERE nro_inv=%"
    cursor.execute(sql, (nro_inv,))
    connection.commit()
    return "Notebook borrada con éxito!"




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

# Ruta para borrar un libro

@app.route('/libros/borrar/<id>', methods=['GET', 'POST'])
def borrar_libro(id):
    if request.method == 'POST':
        eliminar_libro(id)
        return redirect(url_for('libros'))  # Redirige a la lista de libros
    else:
        libro = buscar_libro(id)
        if libro:
            return render_template('confirmar_borrado.html', libro=libro)  # Renderiza una plantilla de confirmación
        else:
            return "Libro no encontrado"
        


@app.route('/instrumentos', methods=['GET', 'POST'])
def instrumentos():
    try:
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
            
            crear_instrumento(nro_inv, cod_rec, tipo, descripcion, marca, modelo, sn, ab_rango, cod_manual, especificaciones, estado, ubicacion, adicionales, fecha_ingreso)  # Función para crear un nuevo instrumento
            return "Instrumento creado exitosamente"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error processing request", 500
    
# Ruta para borrar/buscar un instrumento

@app.route('/libros/borrar/<id>', methods=['GET', 'POST'])
def borrar_libro(id):
    if request.method == 'POST':
        eliminar_libro(id)
        return redirect(url_for('libros'))  # Redirige a la lista de libros
    else:
        libro = buscar_libro(id)
        if libro:
            return render_template('confirmar_borrado.html', libro=libro)  # Renderiza una plantilla de confirmación
        else:
            return "Libro no encontrado"

@app.route('/notebooks', methods=['GET', 'POST'])
def notebooks():
    try:
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
    except Exception as e:
        print(f"Ocurrio el error:  {e}")
        return "Error al procesar requerimiento", 500
    
@app.route('/proyectores', methods=['GET', 'POST'])
def proyectores():
    try:    
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
    except Exception as e:
        print(f"Ocurrio el error:  {e}")
        return "Error al procesar requerimiento", 500

if __name__ == '__main__':
    app.run(debug=True)
    
connection.close()
