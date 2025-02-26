"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: 
inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. 
El nombre de la clase llamarla Triangulo.
"""

class Triangulo:
    def inicializar(self):
        self.lado1 = int(input("\nIngrese el primer lado:"))
        self.lado2 = int(input("Ingrese el segundo lado:"))
        self.lado3 = int(input("Ingrese el tercer lado:"))
    
    def imprimir_mayor(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("\nEl triangulo tiene la misma longitud en todos su lados.")
        else:
            print(f"\nEl lado mayor del triangulo es de {max(self.lado1, self.lado2, self.lado3)}.")
    
    def verificar_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triangulo equilatero.")
        else:
            print("Al menos un lado de los triangulos no es igual.")

#########################   Main    ################################

triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir_mayor()
triangulo1.verificar_equilatero()

triangulo2 = Triangulo()
triangulo2.inicializar()
triangulo2.imprimir_mayor()
triangulo2.verificar_equilatero()

triangulo3 = Triangulo()
triangulo3.inicializar()
triangulo3.imprimir_mayor()
triangulo3.verificar_equilatero()
