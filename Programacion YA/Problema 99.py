"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class Administrador:
    def __init__(self):
        self.nombres = []
        self.telefonos = []
        self.emails = []
    
    def menu(self):
        while True:
            print("\n1- Cargar un contacto en la agenda")
            print("2- Mostrar listado completo de la agenda")
            print("3- Realizar una consulta")
            print("4- Modificar el telefono/email de un contacto")
            print("5- Finalizar programa")
            opcion = int(input("\nIngrese su opcion: "))
            
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listado()
            elif opcion == 3:
                self.consultar()
            elif opcion == 4:
                self.modificar()
            elif opcion == 5:
                print("Programa finalizado.")
                break
    
    def cargar(self):
        nombre = input("\nIngrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono: ")
        email = input("Ingrese el email: ")
        self.nombres.append(nombre)
        self.telefonos.append(telefono)
        self.emails.append(email)
    
    def listado(self):
        if len(self.nombres) == 0:
            print("\nNo hay contactos en la agenda.")
        else:
            print("\nListado de contactos: ")
            for x in range(len(self.nombres)):
                print(f"\nNombre: {self.nombres[x]}")
                print(f"Telefono: {self.telefonos[x]}")
                print(f"Email: {self.emails[x]}")
    
    def consultar(self):
        nom = input("\nIngrese el nombre del contacto: ")
        if nom in self.nombres:
            for nombre in self.nombres:
                if nombre == nom:
                    print(f"\nNombre: {nombre}")
                    print(f"Telefono: {self.telefonos[self.nombres.index(nombre)]}")
                    print(f"Email: {self.emails[self.nombres.index(nombre)]}")
        else:
            print("\nEl contacto no se encuentra.")
    
    def modificar(self):
        nom = input("\nIngrese el nombre del contacto a modificar: ")
        if nom in self.nombres:
            print("\n1- Modificar telefono")
            print("2- Modificar email")
            opcion = int(input("Ingrese su opcion:"))
            if opcion == 1:
                telefono = input("\nIngrese el nuevo telefono: ")
                self.telefonos[self.nombres.index(nom)] = telefono
            if opcion == 2:
                email = input("\nIngrese el nuevo email: ")
                self.emails[self.nombres.index(nom)] = email
        else:
            print("El nombre ingresado no se encuentra en la agenda.")

#########################   Main    ################################

administrador1 = Administrador()
administrador1.menu()