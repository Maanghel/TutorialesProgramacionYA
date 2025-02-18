"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.
"""

# Funcion que calcula el perimetro de un cuadrado
def perimetro_cuadrado(lado):
    return lado * 4

# Funcion que carga el lado de un cuadrado
def carga():
    lado = int(input("Ingrese el lado del cuadrado: "))
    
    return lado

#########################   Main    ################################

lado = carga()

print(f"\nEl perimetro del cuadrado es de {perimetro_cuadrado(lado)}")