"""
Declarar una clase Cuenta y dos subclases CajaAhorro y PlazoFijo. 
Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. 
Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
"""

class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto
    
    def imprimir(self):
        # Funcion que imprime los datos del titular
        print(f"Titular: {self.titular}")
        print(f"Monto: {self.monto}")

# SubClase de la SuperClase Cuenta
class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
    
    def imprimir(self):
        # Funcion que imprime los datos de la caja de ahorro del titular
        print("Cuenta de ahorro:")
        super().imprimir()
        print("No genera intereses.")

# SubClase de la Superclase Cuenta
class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, interes):
        super().__init__(titular, monto) # con la funcion super se indica que se usara un metodo de la clase padre
        self.interes = interes
        self.plazo = plazo
    
    def imprimir(self):
        # Funcion que imprime los datos del titular
        print("\nCuenta de plazo fijo")
        super().imprimir()
        print(f"Plazo en dias: {self.plazo}")
        print(f"Interes: {self.interes}%")
        self.ganancia_interes()

    def ganancia_interes(self):
        # funcion que imprime el importe de los intereses
        ganancia = self.monto * self.interes / 100
        print(f"Importe del interes: {ganancia}")

#########################   Main    ################################

cajaAhorro1 = CajaAhorro("Manuel", 2000)
cajaAhorro1.imprimir()

plazoFijo1 = PlazoFijo("Edmmee", 3000, 45, 0.80)
plazoFijo1.imprimir()