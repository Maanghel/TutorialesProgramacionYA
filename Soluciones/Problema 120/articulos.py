import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="bd1")
        return conexion


    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo= %s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT codigo, descripcion, precio FROM articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM articulos WHERE codigo= %s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount

    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE articulos SET descripcion= %s, precio= %s where codigo= %s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount