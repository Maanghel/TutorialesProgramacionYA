import psycopg2

class Articulos:

    def abrir(self):
        conexion = psycopg2.connect(database= "bd1", user= "postgres", password= "")
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        cone.commit()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo= %s"
        cursor.execute(sql, datos)
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT codigo, descripcion, precio FROM articulos"
        cursor.execute(sql)
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