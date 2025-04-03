"""
Confeccionar una clase que permita carga el nombre y la edad de una persona. 
Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(f"\nEl nombre de la persona es: {self.nombre}")
        print(f"La edad de {self.nombre} es de {self.edad} años")
    
    def mayor_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} es menor de edad")

#########################   Main    ################################

persona1 = Persona()
persona1.inicializar("Manuel", 29)
persona1.imprimir()
persona1.mayor_edad()

persona2 = Persona()
persona2.inicializar("Edmmee", 30)
persona2.imprimir()
persona2.mayor_edad()

persona3 = Persona()
persona3.inicializar("Deylan", 9)
persona3.imprimir()
persona3.mayor_edad()

persona4 = Persona()
persona4.inicializar("Astrid", 1)
persona4.imprimir()
persona4.mayor_edad()