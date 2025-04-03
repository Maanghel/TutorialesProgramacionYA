"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: 
inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado),
imprimir su perímetro y su superficie.
"""

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def perimetro(self):
        # Funcion que imprime el perimetro de un cuadrado
        print(f"\nEl perimetro del cuadrado es de: {self.lado * 4}")
    
    def superficie(self):
        # Funcion que imprime el perimetro de un cuadrado
        print(f"El area del cuadrado es de: {self.lado * self.lado}")

#########################   Main    ################################

cuadrado1 = Cuadrado(2)
cuadrado1.perimetro()
cuadrado1.superficie()

cuadrado2 = Cuadrado(4)
cuadrado2.perimetro()
cuadrado2.superficie()

cuadrado3 = Cuadrado(6)
cuadrado3.perimetro()
cuadrado3.superficie()