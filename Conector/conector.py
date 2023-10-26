import sqlite3 as sql

class Conexion_BD():

    def __init__(self,nombre_bd):
        self.conexion = sql.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
       data= self.cursor.execute(consulta)
       self.commit()
       return data
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()   