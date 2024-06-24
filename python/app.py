import mysql.connector
import flask_cors
from flask import Flask, render_template, request
app = Flask(__name__)



db=mysql.connector.connect(
       host="localhost",
       user="tu_usuario",
       password="tu_contraseña",
       database="tu_base_de_datos"
   )
cursor = db.cursor()

@app.route('/cargar', methods=['GET', 'POST'])
def cargarDatos():
       # Lógica para cargar datos en la base de datos
       return 'Formulario de carga de datos'

@app.route('/alterar', methods=['GET', 'POST'])
def cambiarDatos(id):
       # Lógica para modificar datos en la base de datos
       return 'Formulario de modificación de datos'

@app.route('/eliminar', methods=['GET', 'POST'])
def borrarDatos(id):
       # Lógica para eliminar datos de la base de datos
       return 'Formulario de eliminación de datos'


@app.route('/accion', methods=['POST'])
def accion():
    if request.form['accion'] == 'modificar':
        cambiarDatos(id)
    elif request.form['accion'] == 'eliminar':
        borrarDatos(id)
