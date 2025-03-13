"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, 
calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
"""

class Operaciones:
    def __init__(self):
        self.valor1 = int(input("\nIngrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
    
    def suma(self):
        # Funcion que imprime la suma de dos valores
        print(f"La suma de {self.valor1} mas {self.valor2} es: {self.valor1 + self.valor2}")
    
    def resta(self):
        # Funcion que imprime la resta de dos valores
        print(f"La resta de {self.valor1} menos {self.valor2} es: {self.valor1 - self.valor2}")
    
    def multiplicación(self):
        # Funcion que imprime la multiplicacion de dos valores
        print(f"La multiplicacion de {self.valor1} por {self.valor2} es: {self.valor1 * self.valor2}")
    
    def división(self):
        # Funcion que imprime la division de dos valores
        print(f"La division de {self.valor1} entre {self.valor2} es: {self.valor1 / self.valor2}")

#########################   Main    ################################

operacion1 = Operaciones()
operacion1.suma()
operacion1.resta()
operacion1.multiplicación()
operacion1.división()

operacion2 = Operaciones()
operacion2.suma()
operacion2.resta()
operacion2.multiplicación()
operacion2.división()

operacion3 = Operaciones()
operacion3.suma()
operacion3.resta()
operacion3.multiplicación()
operacion3.división()