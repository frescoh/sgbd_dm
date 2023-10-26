from conector import Conexion_BD as conn

nombre_database = input("Ingrese el nombre de la base de datos para abrirla o crearla: ")
conector = conn(nombre_database+".sqlite3")