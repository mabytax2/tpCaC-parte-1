
# import mysql.connector


# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="labelec"
# )

# cursor = conexion.cursor()

# tabla = "libros"
# consulta = f"SELECT * FROM {tabla}"

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
        

registro_array=[Registros(1,"d1","español","sarasa1","ar02","analizador de espectros"),Registros(2,"d2","ingles","saraza1","ar01","contador")]
for reg in registro_array:
    print(reg.id)

#registro.append(Registros(1, "proyector", "español", "instrumento", "ar01", "proyector view sonic"))
#print(registro)
             

# cursor.execute(consulta)

# # Obtener todos los resultados de la consulta
# resultados = cursor.fetchall()

# # Mostrar los datos de la tabla
# #for fila in resultados:
#     # print(fila)
#     #
    
# with open("tabla1.html", "w") as archivo_html:
#     archivo_html.write("""
#     <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Base de Datos</title>
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Jacquard+24+Charted&display=swap');
#     </style>
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha384-xrR+xx+K1uOoW3pXs9b2D7FjO8j4lYi6kKxX+2Z7yZ7z9IfwL1gk7bDySv+5zv1U" crossorigin="anonymous">
#     <link rel="stylesheet" href="./css/estilos.css">
#     <script src="https://kit.2fontawesome.com/28d049d17c.js" crossorigin="anonymous"></script>
#     </head>
#     <body>
#     <header class="header">
#     <a href="./index.html">
#     <img src="./img/letra-e.gif " height="50px" width="50px" alt="">
#     Home
#     </a>
#     </header>
#     <main>
#     <div class="container">
#     <div class="column">
#     <br>
#     <img class="banner-ing-elec" src="./img/unlam banner vertical.jpg" alt="Ingenieria Electronica">
#     </div>
#     <div class="column">
#     <br><br><br><br>
#     <h1 class="titulos">Registros de la Tabla</h1>
#     <table class="tabla">
#     <tr class="custom-tr">
#     <th class="custom-th">ID</th>
#     <th class="custom-th">Descripcion</th>
#     <th class="custom-th">Idioma</th>
#     <th class="custom-th">Tipo</th>
#     <th class="custom-th">ubicacion</th>
#     <th class="custom-th">Instrumento asociado</th>
#     </tr>
#     """)
    
#     for fila in resultados:
#         archivo_html.write(f"<tr><td>{fila[0]}</td><td>{fila[1]}</td><td>{fila[2]}</td><td>{fila[3]}</td><td>{fila[4]}</td><td>{fila[5]}</td><br></tr>")
#     archivo_html.write("</table></div></body></html>")

# print("Archivo HTML generado con los registros de la tabla.")

# cursor.close()
# conexion.close()
